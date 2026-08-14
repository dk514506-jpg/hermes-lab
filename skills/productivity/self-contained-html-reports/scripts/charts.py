"""charts.py — stdlib-only SVG rendering for self-contained reports.

Zero external dependencies. Every function returns a self-contained SVG
string (no external refs) ready to embed in HTML. Validate with
xml.etree.ElementTree.fromstring() in your verification step.
"""
import html

PALETTE = ["#2563eb", "#f59e0b", "#10b981", "#ef4444", "#8b5cf6", "#0ea5e9", "#64748b"]
GREY = "#6b7280"
GRID = "#e5e7eb"
TEXT = "#374151"


def _e(s):
    return html.escape(str(s))


def _frame(title, width, height, inner):
    return (f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="sans-serif" font-size="11">'
            f'<text x="16" y="18" font-size="13" font-weight="bold" fill="#111827">{_e(title)}</text>'
            f'{inner}</svg>')


def bar_chart(title, labels, series, width=760, height=300):
    """Grouped bar chart. series = [(name, [values])], values aligned to labels."""
    pad_l, pad_b, pad_t, pad_r = 60, 46, 34, 16
    plot_w, plot_h = width - pad_l - pad_r, height - pad_t - pad_b
    n = max(len(labels), 1)
    vals = [v for _, vs in series for v in vs] or [1]
    vmax = max(vals) * 1.15 or 1
    gw, bw = plot_w / n, (plot_w / n) / (len(series) + 1) * 0.8
    y = lambda v: pad_t + plot_h - (v / vmax) * plot_h
    p = [f'<line x1="{pad_l}" y1="{pad_t+plot_h}" x2="{width-pad_r}" y2="{pad_t+plot_h}" stroke="{TEXT}"/>']
    for g in range(5):
        gy = pad_t + plot_h * g / 4
        p.append(f'<line x1="{pad_l}" y1="{gy:.1f}" x2="{width-pad_r}" y2="{gy:.1f}" stroke="{GRID}"/>')
        p.append(f'<text x="{pad_l-6}" y="{gy+3:.1f}" text-anchor="end" fill="{GREY}">{vmax*(1-g/4):.0f}</text>')
    for gi, label in enumerate(labels):
        x0 = pad_l + gi * gw
        for si, (name, vs) in enumerate(series):
            bx = x0 + gw * (si + 0.5) / (len(series) + 1) - bw / 2
            v = vs[gi] if gi < len(vs) else 0
            p.append(f'<rect x="{bx:.1f}" y="{y(v):.1f}" width="{bw:.1f}" height="{pad_t+plot_h-y(v):.1f}" '
                     f'fill="{PALETTE[si % len(PALETTE)]}" rx="2"><title>{_e(name)}: {v:.0f}</title></rect>')
        p.append(f'<text x="{x0+gw/2:.1f}" y="{pad_t+plot_h+14}" text-anchor="middle" fill="{TEXT}">{_e(str(label)[:16])}</text>')
    lx = pad_l
    for si, (name, _) in enumerate(series):
        p.append(f'<rect x="{lx}" y="{height-22}" width="10" height="10" fill="{PALETTE[si % len(PALETTE)]}"/>')
        p.append(f'<text x="{lx+14}" y="{height-13}" fill="{TEXT}">{_e(name)}</text>')
        lx += 14 + len(name) * 6.4 + 20
    return _frame(title, width, height, "".join(p))


def line_chart(title, labels, values, width=760, height=250):
    """Single-series trend line (handles negative values)."""
    pad_l, pad_b, pad_t, pad_r = 60, 40, 34, 16
    plot_w, plot_h = width - pad_l - pad_r, height - pad_t - pad_b
    if len(values) < 2:
        return _frame(title, width, height,
                      f'<text x="{pad_l}" y="{pad_t+plot_h/2}" fill="{GREY}">need 2+ data points</text>')
    lo, hi = min(values + [0]), max(values + [0])
    span = (hi - lo) * 1.2 or 1
    mid = (hi + lo) / 2
    x = lambda i: pad_l + plot_w * i / (len(values) - 1)
    y = lambda v: pad_t + plot_h - ((v - (mid - span / 2)) / span) * plot_h
    p = [f'<line x1="{pad_l}" y1="{pad_t+plot_h}" x2="{width-pad_r}" y2="{pad_t+plot_h}" stroke="{TEXT}"/>']
    for g in range(5):
        gy = pad_t + plot_h * g / 4
        val = (mid + span / 2) - span * g / 4
        p.append(f'<line x1="{pad_l}" y1="{gy:.1f}" x2="{width-pad_r}" y2="{gy:.1f}" stroke="{GRID}"/>')
        p.append(f'<text x="{pad_l-6}" y="{gy+3:.1f}" text-anchor="end" fill="{GREY}">{val:.0f}</text>')
    pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(values))
    p.append(f'<polyline points="{pts}" fill="none" stroke="{PALETTE[0]}" stroke-width="2"/>')
    for i, v in enumerate(values):
        color = PALETTE[1] if v < 0 else PALETTE[0]
        p.append(f'<circle cx="{x(i):.1f}" cy="{y(v):.1f}" r="3.5" fill="{color}"><title>{_e(labels[i])}: {v:.2f}</title></circle>')
        p.append(f'<text x="{x(i):.1f}" y="{pad_t+plot_h+16}" text-anchor="middle" fill="{TEXT}">{_e(str(labels[i])[-5:])}</text>')
    return _frame(title, width, height, "".join(p))


def coverage_chart(title, items, width=760, height=280, ref_label="100% floor"):
    """Coverage bars with a dashed reference line. items = [(label, pct)]."""
    pad_l, pad_b, pad_t, pad_r = 60, 44, 34, 16
    plot_w, plot_h = width - pad_l - pad_r, height - pad_t - pad_b
    n = max(len(items), 1)
    bw = plot_w / n * 0.6
    y = lambda v: pad_t + plot_h - min(v, 150) / 150 * plot_h
    p = [f'<line x1="{pad_l}" y1="{pad_t+plot_h}" x2="{width-pad_r}" y2="{pad_t+plot_h}" stroke="{TEXT}"/>']
    ref_y = y(100)
    p.append(f'<line x1="{pad_l}" y1="{ref_y:.1f}" x2="{width-pad_r}" y2="{ref_y:.1f}" '
             f'stroke="{PALETTE[1]}" stroke-dasharray="4 3"/>')
    p.append(f'<text x="{width-pad_r-2}" y="{ref_y-4:.1f}" text-anchor="end" fill="{PALETTE[1]}">{_e(ref_label)}</text>')
    for g in range(3):
        gy = pad_t + plot_h * g / 2
        p.append(f'<text x="{pad_l-6}" y="{gy+3:.1f}" text-anchor="end" fill="{GREY}">{150*(1-g/2):.0f}</text>')
    for i, (label, pct) in enumerate(items):
        cx = pad_l + plot_w * (i + 0.5) / n
        color = PALETTE[0] if pct >= 100 else (PALETTE[1] if pct >= 70 else PALETTE[3])
        p.append(f'<rect x="{cx-bw/2:.1f}" y="{y(pct):.1f}" width="{bw:.1f}" height="{pad_t+plot_h-y(pct):.1f}" '
                 f'fill="{color}" rx="2"><title>{_e(label)}: {pct}%</title></rect>')
        p.append(f'<text x="{cx:.1f}" y="{pad_t+plot_h+14}" text-anchor="middle" fill="{TEXT}">{_e(str(label)[:12])}</text>')
        p.append(f'<text x="{cx:.1f}" y="{max(y(pct)-5, 12):.1f}" text-anchor="middle" fill="{TEXT}">{pct}%</text>')
    return _frame(title, width, height, "".join(p))


def flow_diagram(title, stages, width=1000, height=200):
    """Horizontal value-stream flow. stages = [(key, name, detail)]."""
    n = len(stages)
    pad = 18
    bw = (width - pad * (n + 1)) / n
    bh, by = 110, 44
    p = []
    for i, (key, name, detail) in enumerate(stages):
        x = pad + i * (bw + pad)
        p.append(f'<rect x="{x:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" rx="6" '
                 f'fill="{PALETTE[i % len(PALETTE)]}" opacity="0.12"/>')
        p.append(f'<rect x="{x:.1f}" y="{by}" width="{bw:.1f}" height="{bh}" rx="6" fill="none" '
                 f'stroke="{PALETTE[i % len(PALETTE)]}" stroke-width="1.5"/>')
        p.append(f'<text x="{x+bw/2:.1f}" y="{by+24}" text-anchor="middle" font-size="12" font-weight="bold" fill="#111827">{_e(key)}</text>')
        p.append(f'<text x="{x+bw/2:.1f}" y="{by+44}" text-anchor="middle" font-size="11" fill="{TEXT}">{_e(name)}</text>')
        p.append(f'<text x="{x+bw/2:.1f}" y="{by+60}" text-anchor="middle" font-size="9" fill="{GREY}">{_e(detail[:40])}</text>')
        if i < n - 1:
            ax = x + bw
            p.append(f'<line x1="{ax:.1f}" y1="{by+bh/2}" x2="{ax+pad:.1f}" y2="{by+bh/2}" stroke="{GREY}" stroke-width="1.5"/>')
            p.append(f'<polygon points="{ax+pad-2:.1f},{by+bh/2-3.5} {ax+pad+1:.1f},{by+bh/2} {ax+pad-2:.1f},{by+bh/2+3.5}" fill="{GREY}"/>')
    return _frame(title, width, height, "".join(p))
