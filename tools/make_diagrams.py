"""Draw the simplified system diagrams used on research pages and as paper thumbnails.

Each diagram is written twice from the same drawing:
  _includes/diagrams/<name>.svg            inline on research pages; colors come from the
                                           --dg-* CSS variables in _sass/_site.scss, so it
                                           follows the site's light/dark toggle
  assets/img/publication_preview/<name>.svg standalone file for <img> use (paper thumbnails,
                                           research cards); falls back to light colors

These are schematic: they show structure, not measured data. Run from the site root:

    python tools/make_diagrams.py
"""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INLINE = ROOT / "_includes" / "diagrams"
STANDALONE = ROOT / "assets" / "img" / "publication_preview"
W = 640

STYLE = """
.dg text{font-family:Roboto,Helvetica,Arial,sans-serif}
.dg .bx{fill:var(--dg-box,#ffffff);stroke:var(--dg-line,#c9c8c2);stroke-width:1.2}
.dg .hl{fill:var(--dg-hl,#e3eefb);stroke:var(--dg-hl-line,#2a78d6);stroke-width:1.4}
.dg .op{fill:var(--dg-op,#fdeae1);stroke:var(--dg-op-line,#eb6834);stroke-width:1.4}
.dg .grp{fill:var(--dg-grp,#f4f4f1);stroke:var(--dg-line,#c9c8c2);stroke-width:1.2;stroke-dasharray:5 4}
.dg .tx{fill:var(--dg-text,#1f2328)}
.dg .sb{fill:var(--dg-muted,#6b6a65)}
.dg .gl{fill:var(--dg-muted,#6b6a65);font-weight:500}
.dg .ar{stroke:var(--dg-arrow,#8f8e89);fill:none;stroke-width:1.6}
.dg .ar.h{stroke:var(--dg-hl-line,#2a78d6)}
.dg .ar.o{stroke:var(--dg-op-line,#eb6834)}
.dg .arh{fill:var(--dg-arrow,#8f8e89)}
.dg .arh.h{fill:var(--dg-hl-line,#2a78d6)}
.dg .arh.o{fill:var(--dg-op-line,#eb6834)}
""".strip()


def esc(s) -> str:
    return html.escape(str(s), quote=True)


class Diagram:
    def __init__(self, name: str, h: int, title: str, desc: str):
        self.name, self.h, self.title, self.desc = name, h, title, desc
        self.parts: list[str] = []

    # -- primitives ---------------------------------------------------------
    def group(self, x, y, w, h, label=""):
        self.parts.append(f'<rect class="grp" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>')
        if label:
            self.parts.append(f'<text class="gl" x="{x + 12}" y="{y + 18}" font-size="12">{esc(label)}</text>')

    def box(self, x, y, w, h, label, sub=None, kind="bx", size=13):
        self.parts.append(f'<rect class="{kind}" x="{x}" y="{y}" width="{w}" height="{h}" rx="7"/>')
        cx = x + w / 2
        if sub:
            self.parts.append(f'<text class="tx" x="{cx}" y="{y + h / 2 - 2}" text-anchor="middle" '
                              f'font-size="{size}" font-weight="500">{esc(label)}</text>')
            self.parts.append(f'<text class="sb" x="{cx}" y="{y + h / 2 + 13}" text-anchor="middle" '
                              f'font-size="11">{esc(sub)}</text>')
        else:
            self.parts.append(f'<text class="tx" x="{cx}" y="{y + h / 2 + 4.5}" text-anchor="middle" '
                              f'font-size="{size}" font-weight="500">{esc(label)}</text>')

    def arrow(self, pts, tone="", both=False, label=None, at=None, anchor="middle"):
        cls = f"ar {tone}".strip()
        mk = f"{self.name}-m{tone or 'n'}"
        p = " ".join(f"{x},{y}" for x, y in pts)
        start = f' marker-start="url(#{mk})"' if both else ""
        self.parts.append(f'<polyline class="{cls}" points="{p}" marker-end="url(#{mk})"{start}/>')
        if label:
            x, y = at
            self.parts.append(f'<text class="sb" x="{x}" y="{y}" text-anchor="{anchor}" '
                              f'font-size="11">{esc(label)}</text>')

    def text(self, x, y, s, cls="sb", size=11, anchor="middle"):
        self.parts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}" '
                          f'font-size="{size}">{esc(s)}</text>')

    def rule(self, x1, y1, x2, y2):
        """Dashed guide line (e.g. a synchronization point)."""
        self.parts.append(f'<line class="ar" stroke-dasharray="5 4" x1="{x1}" y1="{y1}" '
                          f'x2="{x2}" y2="{y2}"/>')

    # -- output -------------------------------------------------------------
    def svg(self, standalone: bool) -> str:
        defs = []
        for tone in ("n", "h", "o"):
            c = "arh" + ("" if tone == "n" else f" {tone}")
            defs.append(f'<marker id="{self.name}-m{tone}" viewBox="0 0 10 10" refX="9" refY="5" '
                        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                        f'<path class="{c}" d="M0,0 L10,5 L0,10 z"/></marker>')
        head = (f'<svg class="dg" viewBox="0 0 {W} {self.h}" role="img" '
                f'aria-labelledby="{self.name}-t {self.name}-d" xmlns="http://www.w3.org/2000/svg">'
                f'<title id="{self.name}-t">{esc(self.title)}</title>'
                f'<desc id="{self.name}-d">{esc(self.desc)}</desc>'
                f'<style>{STYLE}</style><defs>{"".join(defs)}</defs>')
        bg = f'<rect x="0" y="0" width="{W}" height="{self.h}" fill="#ffffff"/>' if standalone else ""
        return head + bg + "\n".join(self.parts) + "</svg>\n"


D: list[Diagram] = []


# --- SmartFuse-LLM: fuse add + RMSNorm into the switch collective -------------------
d = Diagram("smartfuse-llm", 236, "SmartFuse-LLM",
            "Four GPUs send partial results to a programmable switch, which reduces them, applies "
            "the residual add and RMSNorm, and broadcasts the normalized result back: one network "
            "round trip per boundary instead of two.")
for i in range(4):
    x = 40 + i * 150
    d.box(x, 18, 120, 40, f"GPU {i}", kind="bx")
    d.arrow([(x + 42, 58), (x + 42, 96)])
    d.arrow([(x + 78, 96), (x + 78, 58)], tone="h")
d.group(30, 98, 580, 96, "Programmable switch (FPGA datapath)")
d.box(48, 130, 116, 46, "Reduce", kind="hl")
d.box(188, 130, 100, 46, "Add", sub="residual", kind="op")
d.box(312, 130, 120, 46, "RMSNorm", kind="op")
d.box(456, 130, 136, 46, "Broadcast", kind="hl")
d.arrow([(164, 153), (186, 153)])
d.arrow([(288, 153), (310, 153)])
d.arrow([(432, 153), (454, 153)])
d.text(320, 220, "Partial results go in, normalized activations come out: one round trip instead of two")
D.append(d)

# --- PoolStateLens: training state in a switch-attached memory pool -----------------
d = Diagram("poolstatelens", 262, "PoolStateLens",
            "GPUs keep only their active layer. An NVLink switch multicasts parameters from a "
            "switch-attached memory pool and reduces gradients back into it, where an optimizer "
            "updates parameters and optimizer state.")
for i, lab in enumerate(["GPU 0", "GPU 1", "GPU …", "GPU N"]):
    x = 40 + i * 145
    d.box(x, 16, 125, 46, lab, sub="active layer only")
d.box(30, 92, 580, 38, "NVLink switch fabric  ·  multicast parameters, reduce gradients", kind="hl", size=12)
for i in range(4):
    x = 40 + i * 145
    d.arrow([(x + 45, 92), (x + 45, 64)], tone="h")
    d.arrow([(x + 80, 64), (x + 80, 90)])
d.group(110, 156, 420, 92, "Switch-attached memory pool")
d.box(128, 186, 116, 46, "Parameters")
d.box(262, 186, 140, 46, "Optimizer state", sub="master weights, moments")
d.box(420, 186, 92, 46, "Adam", kind="op")
d.arrow([(250, 156), (250, 132)], tone="h", label="parameters", at=(244, 148), anchor="end")
d.arrow([(390, 132), (390, 154)], label="gradients", at=(396, 148), anchor="start")
D.append(d)

# --- SGC: SmartNIC in the ZeRO training data path ----------------------------------
d = Diagram("sgc", 236, "SmartNIC–GPU–CPU co-design",
            "Inside a training node, a SmartNIC prefetches and buffers parameters from the network "
            "and host memory and schedules them to the GPU, overlapping communication with "
            "computation.")
d.group(20, 14, 452, 206, "Training node")
d.box(42, 46, 156, 52, "GPU", sub="forward / backward")
d.box(42, 150, 156, 52, "CPU + host memory", sub="offloaded state")
d.box(270, 92, 182, 66, "SmartNIC", sub="prefetch · buffer · schedule", kind="hl")
d.box(510, 92, 112, 66, "Network", sub="other nodes")
d.arrow([(270, 110), (200, 76)], tone="h", label="parameters", at=(252, 80), anchor="start")
d.arrow([(200, 172), (268, 140)], both=True, label="state", at=(238, 172))
d.arrow([(452, 125), (508, 125)], both=True)
D.append(d)

# --- KernelSight-LM: component models feed a discrete-event simulator ---------------
d = Diagram("kernelsight-lm", 212, "KernelSight-LM",
            "Kernel-latency, communication and host-overhead models feed a discrete-event scheduler "
            "that predicts end-to-end LLM inference latency and throughput.")
d.box(24, 16, 184, 50, "Kernel latency model", sub="profiled GPU kernels")
d.box(24, 81, 184, 50, "Communication model", sub="collectives")
d.box(24, 146, 184, 50, "Host overhead model", sub="launch, scheduling")
d.box(262, 66, 176, 80, "Discrete-event scheduler", sub="batching, KV cache", kind="hl", size=12)
d.box(486, 66, 132, 80, "Predicted", sub="TTFT · TPOT · tput")
for y, ty in ((41, 84), (106, 106), (171, 128)):
    d.arrow([(208, y), (260, ty)])
d.arrow([(438, 106), (484, 106)], tone="h")
D.append(d)

# --- ACBench: agent loop with feedback policies -------------------------------------
d = Diagram("acbench", 220, "ACBench",
            "A task from a real merged pull request goes to an LLM agent, whose patch is applied, "
            "tested and benchmarked against the human patch. A feedback policy decides whether to "
            "retry and what information to send back.")
d.box(18, 30, 120, 52, "Real PR task", sub="production Go code")
d.box(166, 30, 120, 52, "LLM agent", sub="proposes patch", kind="hl")
d.box(314, 30, 130, 52, "Apply + test", sub="benchmark")
d.box(472, 30, 150, 52, "Score", sub="vs. human patch")
d.arrow([(138, 56), (164, 56)])
d.arrow([(286, 56), (312, 56)])
d.arrow([(444, 56), (470, 56)])
d.box(220, 140, 200, 50, "Feedback policy", sub="retry · error message · profile", kind="op")
d.arrow([(379, 82), (379, 138)], tone="o", label="result", at=(386, 114), anchor="start")
d.arrow([(252, 140), (252, 84)], tone="o", label="retry with feedback", at=(245, 114), anchor="end")
d.text(320, 208, "What helps: the extra attempt, or the information?", size=11)
D.append(d)

# --- RL-guided GPU compilation: fingerprints at every lowering stage ----------------
d = Diagram("rl-gpu-compiler", 210, "RL-guided GPU compiler optimization",
            "An RL-guided search proposes changes to a Triton kernel's compilation, from compiler "
            "passes to the final machine code; each change is traced through the compiler stages "
            "and timed on an NVIDIA GB200.")
stages = ["Triton", "TTGIR", "LLVM IR", "PTX", "SASS", "GB200"]
for i, s in enumerate(stages):
    x = 18 + i * 103
    d.box(x, 34, 86, 44, s, kind="hl" if s == "GB200" else "bx")
    if i:
        d.arrow([(x - 17, 56), (x - 2, 56)])
d.text(268, 20, "Trace each change through the compiler", size=11)
d.box(220, 142, 200, 50, "RL-guided search", sub="proposes changes", kind="op")
d.arrow([(260, 142), (163, 80)], tone="o", label="compiler passes", at=(196, 122), anchor="end")
d.arrow([(380, 142), (448, 80)], tone="o", label="machine code", at=(424, 122), anchor="start")
d.arrow([(576, 78), (576, 167), (422, 167)], tone="h", label="runtime", at=(582, 126), anchor="start")
D.append(d)

# --- MPC on FPGA SmartNICs with RDMA -----------------------------------------------
d = Diagram("mpc-fpga", 236, "FPGA-accelerated multi-party computation",
            "Three parties each pair a host with an FPGA SmartNIC that runs the MPC engine. The "
            "SmartNICs exchange secret-shared data over RDMA through a 100 Gb/s switch, bypassing "
            "the CPU.")
for i in range(3):
    x = 24 + i * 204
    d.group(x, 12, 184, 120, f"Party {i + 1}")
    d.box(x + 16, 38, 152, 34, "Host CPU")
    d.box(x + 16, 84, 152, 36, "FPGA SmartNIC", sub=None, kind="hl")
    d.arrow([(x + 92, 72), (x + 92, 82)])
    d.arrow([(x + 92, 132), (x + 92, 168)], tone="h", both=True)
d.box(24, 170, 592, 38, "100 Gb/s switch  ·  RDMA, CPU bypass", kind="bx", size=12)
d.text(320, 228, "Secret-shared data only: no party sees another's inputs")
D.append(d)

# --- Load imbalance in HPC applications: profile idle time, reuse it -----------------
# Schematic of the idea in the paper's title (bar lengths are illustrative, not data).
d = Diagram("load-imbalance", 232, "Load imbalance in HPC applications",
            "Four parallel processes finish their work at different times and the faster ones "
            "wait idle at a synchronization point. A profiler measures that idle time, and the "
            "wasted cycles are reused to run other work.")
x0, sync = 84, 452
for i, work in enumerate((sync - x0, 214, 300, 160)):  # process 0 is the slowest: no idle
    y = 26 + i * 42
    d.text(70, y + 19, f"Process {i}", cls="tx", size=12, anchor="end")
    d.box(x0, y, work, 28, "compute" if i == 0 else "", kind="hl", size=11)
    if sync - x0 - work > 6:
        d.box(x0 + work + 2, y, sync - x0 - work - 2, 28,
              "idle" if work < 250 else "", kind="op", size=11)
d.rule(sync, 14, sync, 192)
d.text(sync, 208, "synchronization point", size=11)
d.box(492, 30, 132, 52, "Profiler", sub="measure idle time")
d.box(492, 116, 132, 52, "Reuse idle cycles", sub="run other work", kind="op", size=12)
d.arrow([(456, 56), (490, 56)])
d.arrow([(558, 82), (558, 114)], tone="o")
d.arrow([(490, 150), (456, 150)], tone="o")
d.text(268, 226, "Faster processes wait; those wasted cycles can do useful work", size=11)
D.append(d)

# --- ML-guided LLVM pass ordering for HLS ------------------------------------------
d = Diagram("rl-hls", 206, "RL pass ordering for high-level synthesis",
            "An RL agent chooses the LLVM pass sequence applied to a C/C++ kernel before "
            "high-level synthesis, and learns from the resulting FPGA design's quality.")
d.box(18, 26, 120, 50, "C/C++ kernel")
d.box(166, 26, 140, 50, "LLVM passes", sub="order chosen by agent", kind="op")
d.box(334, 26, 120, 50, "HLS tool")
d.box(482, 26, 140, 50, "FPGA design", sub="latency · area")
d.arrow([(138, 51), (164, 51)])
d.arrow([(306, 51), (332, 51)])
d.arrow([(454, 51), (480, 51)])
d.box(220, 140, 200, 50, "RL agent", sub="learns pass order", kind="hl")
d.arrow([(260, 140), (236, 78)], tone="h", label="pass sequence", at=(242, 116), anchor="end")
d.arrow([(552, 76), (552, 165), (422, 165)], tone="h", label="reward", at=(558, 124), anchor="start")
D.append(d)


def main() -> None:
    INLINE.mkdir(parents=True, exist_ok=True)
    STANDALONE.mkdir(parents=True, exist_ok=True)
    for d in D:
        (INLINE / f"{d.name}.svg").write_text(
            '<figure class="diagram">' + d.svg(False) + "</figure>\n", encoding="utf-8")
        (STANDALONE / f"{d.name}.svg").write_text(d.svg(True), encoding="utf-8")
        print("wrote", d.name)


if __name__ == "__main__":
    main()
