
import tkinter as tk
from tkinter import ttk
 
 
class Colors:
    # Backgrounds — warm whites and cool light grays
    BG_LIGHT  = "#f5f7fa"   # main app background (cool off-white)
    BG_NAV    = "#ffffff"   # top nav bar (pure white)
    BG_CARD   = "#ffffff"   # card / panel background
    BG_INPUT  = "#f0f2f5"   # text input background
    BG_HOVER  = "#e8ecf2"   # hover state for rows / buttons
 
    # Text
    TEXT_PRI = "#1a1d23"   # primary text (near-black, warm)
    TEXT_MUT = "#6b7280"   # muted / secondary text (medium gray)
    TEXT_DIM = "#b0b8c4"   # very dim text / placeholders
 
    # Accent palette — sky blue / indigo
    ACCENT      = "#2563eb"   # blue — primary CTA
    ACCENT_SOFT = "#dbeafe"   # light blue for backgrounds / badges
    ACCENT_DARK = "#1d4ed8"   # darker blue for pressed/active
 
    # Semantic colors
    SUCCESS      = "#16a34a"   # green
    SUCCESS_SOFT = "#dcfce7"   # light green badge bg
    DANGER       = "#dc2626"   # red
    DANGER_SOFT  = "#fee2e2"   # light red badge bg
    WARNING      = "#d97706"   # amber
    WARNING_SOFT = "#fef3c7"   # light amber badge bg
 
    # Borders & shadows
    BORDER       = "#e2e6ed"   # default border (light gray)
    BORDER_FOCUS = "#2563eb"   # blue border on focused inputs
    SHADOW       = "#d1d5db"   # subtle shadow tone
 
 
class Fonts:
    BRAND   = ("Helvetica", 20, "bold")
    HEADING = ("Helvetica", 15, "bold")
    SUBHEAD = ("Helvetica", 12, "bold")
    BODY    = ("Helvetica", 11)
    MUTED   = ("Helvetica", 10)
    MONO    = ("Courier", 11)
 
 
def apply_theme(root):
    """
    Apply the light theme to the entire Tkinter app.
    Call this once on the root Tk() instance before building any frames.
    """
    root.configure(bg=Colors.BG_LIGHT)
 
    style = ttk.Style(root)
 
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass
 
    # ── Base frames & labels ──────────────────────────────────────────────
    style.configure("TFrame",         background=Colors.BG_LIGHT)
    style.configure("TLabel",         background=Colors.BG_LIGHT, foreground=Colors.TEXT_PRI, font=Fonts.BODY)
    style.configure("Muted.TLabel",   background=Colors.BG_LIGHT, foreground=Colors.TEXT_MUT, font=Fonts.MUTED)
    style.configure("Title.TLabel",   background=Colors.BG_LIGHT, foreground=Colors.ACCENT,   font=Fonts.BRAND)
    style.configure("Heading.TLabel", background=Colors.BG_LIGHT, foreground=Colors.TEXT_PRI, font=Fonts.HEADING)
    style.configure("Dim.TLabel",     background=Colors.BG_LIGHT, foreground=Colors.TEXT_DIM, font=Fonts.MUTED)
 
    # ── Card styles ───────────────────────────────────────────────────────
    style.configure("Card.TFrame",        background=Colors.BG_CARD)
    style.configure("Card.TLabel",        background=Colors.BG_CARD, foreground=Colors.TEXT_PRI, font=Fonts.BODY)
    style.configure("CardHeading.TLabel", background=Colors.BG_CARD, foreground=Colors.TEXT_PRI, font=Fonts.SUBHEAD)
    style.configure("CardMuted.TLabel",   background=Colors.BG_CARD, foreground=Colors.TEXT_MUT, font=Fonts.MUTED)
    style.configure("Accent.TLabel",      background=Colors.BG_CARD, foreground=Colors.ACCENT,   font=Fonts.SUBHEAD)
 
    # ── Nav bar ───────────────────────────────────────────────────────────
    style.configure("Nav.TFrame", background=Colors.BG_NAV)
    style.configure("Nav.TLabel", background=Colors.BG_NAV, foreground=Colors.ACCENT, font=Fonts.SUBHEAD)
 
    # ── Status bar ────────────────────────────────────────────────────────
    style.configure("Status.TFrame", background=Colors.BG_CARD)
    style.configure("Status.TLabel", background=Colors.BG_CARD, foreground=Colors.TEXT_MUT, font=Fonts.MUTED)
 
    # ── Buttons ───────────────────────────────────────────────────────────
    style.configure("TButton",
        background=Colors.BG_CARD,
        foreground=Colors.TEXT_PRI,
        font=Fonts.BODY,
        borderwidth=1,
        relief="flat",
        padding=(10, 5)
    )
    style.map("TButton",
        background=[("active", Colors.BG_HOVER), ("pressed", Colors.SHADOW)],
        relief=[("pressed", "flat")]
    )
 
    # Primary (blue) CTA
    style.configure("Accent.TButton",
        background=Colors.ACCENT,
        foreground="#ffffff",
        font=Fonts.BODY,
        padding=(12, 6)
    )
    style.map("Accent.TButton",
        background=[("active", Colors.ACCENT_DARK), ("pressed", "#1e40af")]
    )
 
    # Ghost / text button
    style.configure("Ghost.TButton",
        background=Colors.BG_LIGHT,
        foreground=Colors.TEXT_MUT,
        font=Fonts.MUTED,
        padding=(8, 4)
    )
    style.map("Ghost.TButton",
        background=[("active", Colors.BG_HOVER)],
        foreground=[("active", Colors.ACCENT)]
    )
 
    # Nav button
    style.configure("Nav.TButton",
        background=Colors.BG_NAV,
        foreground=Colors.TEXT_MUT,
        font=Fonts.MUTED,
        padding=(8, 4)
    )
    style.map("Nav.TButton",
        background=[("active", Colors.BG_HOVER)],
        foreground=[("active", Colors.ACCENT)]
    )
 
    # Success
    style.configure("Success.TButton",
        background=Colors.SUCCESS,
        foreground="#ffffff",
        font=Fonts.BODY,
        padding=(10, 5)
    )
    style.map("Success.TButton",
        background=[("active", "#15803d")]
    )
 
    # Danger / destructive
    style.configure("Danger.TButton",
        background=Colors.DANGER,
        foreground="#ffffff",
        font=Fonts.BODY,
        padding=(10, 5)
    )
    style.map("Danger.TButton",
        background=[("active", "#b91c1c")]
    )
 
    # ── Entry / text inputs ───────────────────────────────────────────────
    style.configure("TEntry",
        fieldbackground=Colors.BG_INPUT,
        foreground=Colors.TEXT_PRI,
        insertcolor=Colors.ACCENT,
        bordercolor=Colors.BORDER,
        lightcolor=Colors.BORDER,
        darkcolor=Colors.BORDER,
        borderwidth=1,
        relief="flat"
    )
    style.map("TEntry",
        fieldbackground=[("focus", "#ffffff")],
        bordercolor=[("focus", Colors.BORDER_FOCUS)],
        lightcolor=[("focus", Colors.BORDER_FOCUS)]
    )
 
    # ── Treeview ──────────────────────────────────────────────────────────
    style.configure("Treeview",
        background=Colors.BG_CARD,
        foreground=Colors.TEXT_PRI,
        fieldbackground=Colors.BG_CARD,
        rowheight=30,
        font=Fonts.BODY
    )
    style.configure("Treeview.Heading",
        background=Colors.BG_LIGHT,
        foreground=Colors.TEXT_MUT,
        font=Fonts.MUTED,
        relief="flat"
    )
    style.map("Treeview",
        background=[("selected", Colors.ACCENT_SOFT)],
        foreground=[("selected", Colors.ACCENT_DARK)]
    )
 
    # ── Combobox & Spinbox ────────────────────────────────────────────────
    style.configure("TCombobox",
        fieldbackground=Colors.BG_INPUT,
        background=Colors.BG_INPUT,
        foreground=Colors.TEXT_PRI,
        selectbackground=Colors.ACCENT_SOFT,
        arrowcolor=Colors.TEXT_MUT
    )
    style.configure("TSpinbox",
        fieldbackground=Colors.BG_INPUT,
        foreground=Colors.TEXT_PRI,
        arrowcolor=Colors.TEXT_MUT
    )
 
    # ── Checkbutton ───────────────────────────────────────────────────────
    style.configure("TCheckbutton",
        background=Colors.BG_CARD,
        foreground=Colors.TEXT_PRI,
        font=Fonts.BODY,
        indicatorcolor=Colors.BG_INPUT
    )
    style.map("TCheckbutton",
        indicatorcolor=[("selected", Colors.ACCENT)]
    )
 
    # ── Scrollbar ─────────────────────────────────────────────────────────
    style.configure("TScrollbar",
        background=Colors.BG_HOVER,
        troughcolor=Colors.BG_LIGHT,
        borderwidth=0,
        arrowsize=12,
        arrowcolor=Colors.TEXT_MUT
    )
    style.map("TScrollbar",
        background=[("active", Colors.ACCENT)]
    )
 
    # ── Separator ─────────────────────────────────────────────────────────
    style.configure("TSeparator", background=Colors.BORDER)
 
    # ── Notebook (tabs) ───────────────────────────────────────────────────
    style.configure("TNotebook",
        background=Colors.BG_LIGHT,
        borderwidth=0
    )
    style.configure("TNotebook.Tab",
        background=Colors.BG_CARD,
        foreground=Colors.TEXT_MUT,
        font=Fonts.MUTED,
        padding=(12, 5)
    )
    style.map("TNotebook.Tab",
        background=[("selected", Colors.BG_LIGHT)],
        foreground=[("selected", Colors.ACCENT)]
    )
 
    # ── Progressbar ───────────────────────────────────────────────────────
    style.configure("TProgressbar",
        troughcolor=Colors.ACCENT_SOFT,
        background=Colors.ACCENT,
        borderwidth=0,
        thickness=6
    )
 
 
# ── Helper widget factories ───────────────────────────────────────────────
 
def make_card(parent, padding=16):
    """
    Returns a styled card frame (white background, sits on the light gray page).
    """
    frame = ttk.Frame(parent, style="Card.TFrame", padding=padding)
    return frame
 
 
def make_scrolled_treeview(parent, columns, heights=10, col_widths=None):
    """
    Returns a Treeview with a vertical scrollbar attached.
    Packs itself into parent automatically.
    """
    wrapper = ttk.Frame(parent)
    wrapper.pack(fill="both", expand=True, padx=16, pady=8)
 
    sb = ttk.Scrollbar(wrapper, orient="vertical")
    sb.pack(side="right", fill="y")
 
    tree = ttk.Treeview(
        wrapper,
        columns=columns,
        show="headings",
        height=heights,
        yscrollcommand=sb.set
    )
    sb.config(command=tree.yview)
 
    for col in columns:
        width = (col_widths or {}).get(col, 100)
        tree.heading(col, text=col)
        tree.column(col, width=width, anchor="w")
 
    tree.pack(fill="both", expand=True)
    return tree
 
 
def make_action_bar(parent, buttons):
    """
    Creates a bottom bar with a list of buttons.
    buttons = list of (label, style, command) tuples.
    """
    bar = ttk.Frame(parent, style="TFrame", padding=(16, 8))
    bar.pack(fill="x", side="bottom")
    for label, style, cmd in buttons:
        ttk.Button(bar, text=label, style=style, command=cmd).pack(side="left", padx=4)
 
 
def styled_text(parent, height=6, width=40):
    """
    Returns a tk.Text widget styled to match the light theme.
    """
    widget = tk.Text(
        parent,
        height=height,
        width=width,
        bg=Colors.BG_INPUT,
        fg=Colors.TEXT_PRI,
        insertbackground=Colors.ACCENT,
        selectbackground=Colors.ACCENT_SOFT,
        selectforeground=Colors.ACCENT_DARK,
        relief="flat",
        font=Fonts.BODY,
        padx=8,
        pady=6,
        wrap="word"
    )
    return widget
 
 
def make_badge(parent, text, color="accent"):
    """
    Returns a small colored label badge (accent / success / danger / warning).
    color: 'accent' | 'success' | 'danger' | 'warning'
    """
    palette = {
        "accent":  (Colors.ACCENT_SOFT,   Colors.ACCENT_DARK),
        "success": (Colors.SUCCESS_SOFT,   "#15803d"),
        "danger":  (Colors.DANGER_SOFT,    "#b91c1c"),
        "warning": (Colors.WARNING_SOFT,   "#92400e"),
    }
    bg, fg = palette.get(color, palette["accent"])
    label = tk.Label(
        parent,
        text=f"  {text}  ",
        bg=bg,
        fg=fg,
        font=Fonts.MUTED,
        relief="flat",
        padx=4,
        pady=2
    )
    return label
