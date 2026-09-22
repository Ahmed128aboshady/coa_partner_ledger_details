
# -*- coding: utf-8 -*-
"""
Generator script for coa_partner_ledger_details Odoo App Store description page.
Writes index.html with UTF-8 encoding (no BOM).
"""

OUTPUT_PATH = r"C:\Users\user\.gemini\antigravity\scratch\coa_addons_repo\coa_partner_ledger_details\static\description\index.html"

HTML = r"""<div style="font-family:'Inter',sans-serif;color:#1a1a2e;background:#ffffff;margin:0;padding:0;box-sizing:border-box;max-width:1100px;margin:0 auto;">

<!-- =====================================================================
     SECTION 1 — HERO HEADER
     ===================================================================== -->
<div style="background:linear-gradient(135deg,#041F33 0%,#063153 55%,#0F5586 100%);border-radius:18px;padding:60px 48px 48px;margin-bottom:40px;position:relative;overflow:hidden;">

  <!-- Decorative circles -->
  <div style="position:absolute;top:-60px;right:-60px;width:320px;height:320px;border-radius:50%;background:rgba(15,85,134,0.25);pointer-events:none;"></div>
  <div style="position:absolute;bottom:-80px;left:-40px;width:260px;height:260px;border-radius:50%;background:rgba(6,49,83,0.40);pointer-events:none;"></div>

  <!-- Logo + badge row -->
  <div style="display:flex;align-items:center;gap:18px;margin-bottom:32px;flex-wrap:wrap;">
    <div style="background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.22);border-radius:50px;padding:8px 18px 8px 8px;display:inline-flex;align-items:center;gap:10px;">
      <img src="coa_logo.jpg" alt="COA Logo" style="height:36px;width:36px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,0.3);" />
      <span style="color:#ffffff;font-size:14px;font-weight:700;letter-spacing:0.5px;">Code Of Arts</span>
    </div>
    <div style="background:rgba(34,197,94,0.18);border:1.5px solid rgba(34,197,94,0.45);border-radius:50px;padding:7px 16px;display:inline-flex;align-items:center;gap:8px;">
      <span style="display:inline-block;width:9px;height:9px;border-radius:50%;background:#22c55e;box-shadow:0 0 8px #22c55e;"></span>
      <span style="color:#86efac;font-size:13px;font-weight:600;letter-spacing:0.3px;">Odoo 19 · 18 · 17 &nbsp;Enterprise Ready</span>
    </div>
    <div style="background:rgba(140,29,34,0.25);border:1.5px solid rgba(230,27,33,0.45);border-radius:50px;padding:7px 16px;">
      <span style="color:#fca5a5;font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;">Enterprise Only</span>
    </div>
  </div>

  <!-- Headline -->
  <h1 style="color:#ffffff;font-size:clamp(26px,4vw,42px);font-weight:800;line-height:1.18;margin:0 0 16px;letter-spacing:-0.5px;max-width:700px;">
    Partner Ledger with<br/>
    <span style="color:#93c5fd;">Invoice Line Drill-down</span>
  </h1>
  <p style="color:#bfdbfe;font-size:17px;font-weight:400;line-height:1.65;max-width:640px;margin:0 0 40px;">
    Extend your Odoo Enterprise Partner Ledger: every invoice becomes expandable.
    One click reveals all product lines — quantity, unit of measure, and line total —
    directly inside the ledger report. No extra screens. No hacks.
  </p>

  <!-- 4 Metric cards -->
  <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:44px;">
    <div style="background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:20px 24px;min-width:160px;flex:1;">
      <div style="color:#93c5fd;font-size:30px;font-weight:800;line-height:1;">&#8734;</div>
      <div style="color:#e0f2fe;font-size:13px;font-weight:600;margin-top:6px;text-transform:uppercase;letter-spacing:0.5px;">Expandable Invoices</div>
    </div>
    <div style="background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:20px 24px;min-width:160px;flex:1;">
      <div style="color:#86efac;font-size:30px;font-weight:800;line-height:1;">&#10003;</div>
      <div style="color:#e0f2fe;font-size:13px;font-weight:600;margin-top:6px;text-transform:uppercase;letter-spacing:0.5px;">Product Line Details</div>
    </div>
    <div style="background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:20px 24px;min-width:160px;flex:1;">
      <div style="color:#fde68a;font-size:30px;font-weight:800;line-height:1;">Qty</div>
      <div style="color:#e0f2fe;font-size:13px;font-weight:600;margin-top:6px;text-transform:uppercase;letter-spacing:0.5px;">Qty + UoM Shown</div>
    </div>
    <div style="background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.18);border-radius:14px;padding:20px 24px;min-width:160px;flex:1;">
      <div style="color:#c4b5fd;font-size:30px;font-weight:800;line-height:1;">&#9670;</div>
      <div style="color:#e0f2fe;font-size:13px;font-weight:600;margin-top:6px;text-transform:uppercase;letter-spacing:0.5px;">Enterprise Native</div>
    </div>
  </div>

  <!-- Mac browser window mockup -->
  <div style="background:rgba(255,255,255,0.07);border:1.5px solid rgba(255,255,255,0.15);border-radius:16px;overflow:hidden;max-width:820px;margin:0 auto 40px;">
    <div style="background:rgba(0,0,0,0.35);padding:10px 16px;display:flex;align-items:center;gap:8px;">
      <span style="width:13px;height:13px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
      <span style="width:13px;height:13px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
      <span style="width:13px;height:13px;border-radius:50%;background:#28c840;display:inline-block;"></span>
      <div style="flex:1;margin:0 14px;background:rgba(255,255,255,0.12);border-radius:6px;padding:4px 12px;text-align:center;">
        <span style="color:rgba(255,255,255,0.55);font-size:12px;">Odoo &#8250; Accounting &#8250; Partner Ledger</span>
      </div>
    </div>
    <img src="02_partner_ledger_expanded.png"
         alt="Partner Ledger with expanded invoice lines showing product details, quantity, UoM and line totals"
         style="width:100%;display:block;object-fit:cover;" />
  </div>

  <!-- Feature tag pills -->
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <span style="background:rgba(99,179,237,0.18);border:1px solid rgba(99,179,237,0.35);color:#93c5fd;border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:0.4px;">&#9654; Drill-down</span>
    <span style="background:rgba(99,179,237,0.18);border:1px solid rgba(99,179,237,0.35);color:#93c5fd;border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:0.4px;">&#128230; Product Lines</span>
    <span style="background:rgba(99,179,237,0.18);border:1px solid rgba(99,179,237,0.35);color:#93c5fd;border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:0.4px;">&#9878; Partner Ledger</span>
    <span style="background:rgba(99,179,237,0.18);border:1px solid rgba(99,179,237,0.35);color:#93c5fd;border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:0.4px;">&#127758; Enterprise</span>
    <span style="background:rgba(99,179,237,0.18);border:1px solid rgba(99,179,237,0.35);color:#93c5fd;border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:0.4px;">&#9881; Official Framework</span>
    <span style="background:rgba(99,179,237,0.18);border:1px solid rgba(99,179,237,0.35);color:#93c5fd;border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:0.4px;">&#128200; Accounting</span>
    <span style="background:rgba(134,239,172,0.15);border:1px solid rgba(134,239,172,0.30);color:#86efac;border-radius:50px;padding:6px 16px;font-size:12px;font-weight:600;letter-spacing:0.4px;">v17 / v18 / v19</span>
  </div>
</div>


<!-- =====================================================================
     SECTION 2 — PROBLEM vs SOLUTION
     ===================================================================== -->
<div style="margin-bottom:40px;">
  <div style="text-align:center;margin-bottom:36px;">
    <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:6px 20px;font-size:12px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;">Pain Point &#8594; Solution</span>
    <h2 style="font-size:clamp(22px,3.5vw,34px);font-weight:800;color:#041F33;margin:16px 0 8px;letter-spacing:-0.3px;">The Problem &amp; How We Solve It</h2>
    <p style="color:#6E93B0;font-size:16px;max-width:560px;margin:0 auto;line-height:1.6;">
      Standard Odoo Enterprise Partner Ledger hides the detail your accounting team actually needs.
    </p>
  </div>

  <div style="display:flex;gap:24px;flex-wrap:wrap;">

    <!-- WITHOUT card -->
    <div style="flex:1;min-width:280px;background:#fff5f5;border:2px solid #fecaca;border-radius:16px;padding:32px 28px;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:24px;">
        <div style="width:44px;height:44px;border-radius:12px;background:#fecaca;display:flex;align-items:center;justify-content:center;">
          <span style="color:#8C1D22;font-size:22px;line-height:1;">&#10005;</span>
        </div>
        <div>
          <div style="font-size:11px;font-weight:700;color:#8C1D22;text-transform:uppercase;letter-spacing:1px;">Without This Module</div>
          <div style="font-size:17px;font-weight:800;color:#7f1d1d;margin-top:2px;">Blind Ledger</div>
        </div>
      </div>
      <ul style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:14px;">
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#fecaca;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#8C1D22;font-size:13px;font-weight:800;">&#10005;</span>
          <span style="color:#7f1d1d;font-size:15px;line-height:1.5;">Cannot see which products are inside an invoice from the ledger view</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#fecaca;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#8C1D22;font-size:13px;font-weight:800;">&#10005;</span>
          <span style="color:#7f1d1d;font-size:15px;line-height:1.5;">Must open each invoice separately — breaking your workflow entirely</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#fecaca;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#8C1D22;font-size:13px;font-weight:800;">&#10005;</span>
          <span style="color:#7f1d1d;font-size:15px;line-height:1.5;">No drill-down capability — the ledger is a flat, context-free list</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#fecaca;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#8C1D22;font-size:13px;font-weight:800;">&#10005;</span>
          <span style="color:#7f1d1d;font-size:15px;line-height:1.5;">Wastes hours of accounting time on repetitive invoice lookups</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#fecaca;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#8C1D22;font-size:13px;font-weight:800;">&#10005;</span>
          <span style="color:#7f1d1d;font-size:15px;line-height:1.5;">No quantity or UoM visible — reconciliation requires manual cross-checking</span>
        </li>
      </ul>
    </div>

    <!-- WITH card -->
    <div style="flex:1;min-width:280px;background:#f0fdf4;border:2px solid #86efac;border-radius:16px;padding:32px 28px;">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:24px;">
        <div style="width:44px;height:44px;border-radius:12px;background:#bbf7d0;display:flex;align-items:center;justify-content:center;">
          <span style="color:#166534;font-size:22px;line-height:1;">&#10003;</span>
        </div>
        <div>
          <div style="font-size:11px;font-weight:700;color:#166534;text-transform:uppercase;letter-spacing:1px;">With This Module</div>
          <div style="font-size:17px;font-weight:800;color:#14532d;margin-top:2px;">Full Visibility</div>
        </div>
      </div>
      <ul style="margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:14px;">
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:13px;font-weight:800;">&#10003;</span>
          <span style="color:#14532d;font-size:15px;line-height:1.5;">One click expands any invoice to show all its product lines inline</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:13px;font-weight:800;">&#10003;</span>
          <span style="color:#14532d;font-size:15px;line-height:1.5;">Qty and line total visible directly in the ledger — zero context switching</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:13px;font-weight:800;">&#10003;</span>
          <span style="color:#14532d;font-size:15px;line-height:1.5;">Instant drill-down — expand, review, collapse, move on</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:13px;font-weight:800;">&#10003;</span>
          <span style="color:#14532d;font-size:15px;line-height:1.5;">Saves hours every month — accountants stay in one report screen</span>
        </li>
        <li style="display:flex;align-items:flex-start;gap:12px;">
          <span style="margin-top:3px;width:22px;height:22px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:13px;font-weight:800;">&#10003;</span>
          <span style="color:#14532d;font-size:15px;line-height:1.5;">UoM displayed per line — perfect for quantity-based reconciliation</span>
        </li>
      </ul>
    </div>
  </div>
</div>


<!-- =====================================================================
     SECTION 3 — 6 FEATURE PILLARS
     ===================================================================== -->
<div style="margin-bottom:40px;">
  <div style="text-align:center;margin-bottom:36px;">
    <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:6px 20px;font-size:12px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;">Features</span>
    <h2 style="font-size:clamp(22px,3.5vw,34px);font-weight:800;color:#041F33;margin:16px 0 8px;letter-spacing:-0.3px;">Six Pillars of Power</h2>
    <p style="color:#6E93B0;font-size:16px;max-width:540px;margin:0 auto;line-height:1.6;">
      Everything carefully designed to fit natively into your Odoo Enterprise accounting workflow.
    </p>
  </div>

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;">

    <!-- Pillar 1 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;padding:28px 24px;transition:box-shadow 0.2s;">
      <div style="width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#0F5586,#6E93B0);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <span style="color:#fff;font-size:24px;">&#9654;</span>
      </div>
      <h3 style="font-size:17px;font-weight:800;color:#041F33;margin:0 0 10px;">Expandable Invoice Lines</h3>
      <p style="color:#6E93B0;font-size:14px;line-height:1.65;margin:0;">
        Every invoice entry in the Partner Ledger gains a clickable expand arrow.
        Toggle open to reveal all child product lines, toggle closed to hide them.
        The report stays clean and scannable until you need the detail.
      </p>
    </div>

    <!-- Pillar 2 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;padding:28px 24px;">
      <div style="width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#041F33,#0F5586);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <span style="color:#fff;font-size:24px;">&#128230;</span>
      </div>
      <h3 style="font-size:17px;font-weight:800;color:#041F33;margin:0 0 10px;">Product Name &amp; Quantity Display</h3>
      <p style="color:#6E93B0;font-size:14px;line-height:1.65;margin:0;">
        Each expanded sub-row shows the full product name alongside the exact
        quantity ordered or delivered. Your team immediately knows what was sold
        or purchased without ever leaving the ledger screen.
      </p>
    </div>

    <!-- Pillar 3 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;padding:28px 24px;">
      <div style="width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#063153,#0F5586);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <span style="color:#fff;font-size:24px;">&#128200;</span>
      </div>
      <h3 style="font-size:17px;font-weight:800;color:#041F33;margin:0 0 10px;">Line Total in Balance Column</h3>
      <p style="color:#6E93B0;font-size:14px;line-height:1.65;margin:0;">
        The monetary total for each product line appears in the existing balance
        column — consistent with the native ledger layout. No extra columns,
        no layout shifts. Just the numbers where you expect them.
      </p>
    </div>

    <!-- Pillar 4 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;padding:28px 24px;">
      <div style="width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#0F5586,#6E93B0);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <span style="color:#fde68a;font-size:20px;font-weight:800;">UoM</span>
      </div>
      <h3 style="font-size:17px;font-weight:800;color:#041F33;margin:0 0 10px;">Unit of Measure Shown</h3>
      <p style="color:#6E93B0;font-size:14px;line-height:1.65;margin:0;">
        The UoM (Unit of Measure) is displayed next to the quantity for every
        expanded product line. Critical for businesses handling items in kg, m²,
        pcs, hours, or custom units — eliminates reconciliation ambiguity instantly.
      </p>
    </div>

    <!-- Pillar 5 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;padding:28px 24px;">
      <div style="width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#6E93B0,#041F33);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <span style="color:#fff;font-size:24px;">&#9881;</span>
      </div>
      <h3 style="font-size:17px;font-weight:800;color:#041F33;margin:0 0 10px;">Official Framework — No Hacks</h3>
      <p style="color:#6E93B0;font-size:14px;line-height:1.65;margin:0;">
        Built entirely on Odoo's official <code style="background:#E7EEF3;border-radius:4px;padding:1px 5px;font-size:13px;color:#0F5586;">account_reports</code> framework.
        No monkey-patching, no template overrides that break on upgrade,
        no JavaScript tricks. This is Odoo the way Odoo was meant to be extended.
      </p>
    </div>

    <!-- Pillar 6 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;padding:28px 24px;">
      <div style="width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,#041F33,#063153);display:flex;align-items:center;justify-content:center;margin-bottom:18px;">
        <span style="color:#86efac;font-size:24px;">&#10038;</span>
      </div>
      <h3 style="font-size:17px;font-weight:800;color:#041F33;margin:0 0 10px;">Enterprise Partner Ledger Integration</h3>
      <p style="color:#6E93B0;font-size:14px;line-height:1.65;margin:0;">
        Seamlessly integrates with the standard Odoo Enterprise Partner Ledger
        report. All filters, groupings, date ranges, and export options continue
        to work exactly as before. Accountants get more — without learning anything new.
      </p>
    </div>

  </div>
</div>


<!-- =====================================================================
     SECTION 4 — HOW IT WORKS (3 Steps, dark bg)
     ===================================================================== -->
<div style="background:linear-gradient(135deg,#041F33 0%,#063153 100%);border-radius:18px;padding:56px 48px;margin-bottom:40px;position:relative;overflow:hidden;">
  <div style="position:absolute;top:-40px;right:-40px;width:240px;height:240px;border-radius:50%;background:rgba(15,85,134,0.20);pointer-events:none;"></div>
  <div style="position:absolute;bottom:-60px;left:-30px;width:200px;height:200px;border-radius:50%;background:rgba(110,147,176,0.12);pointer-events:none;"></div>

  <div style="text-align:center;margin-bottom:48px;">
    <span style="background:rgba(99,179,237,0.15);border:1px solid rgba(99,179,237,0.35);color:#93c5fd;border-radius:50px;padding:6px 20px;font-size:12px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;">How It Works</span>
    <h2 style="font-size:clamp(22px,3.5vw,34px);font-weight:800;color:#ffffff;margin:16px 0 8px;letter-spacing:-0.3px;">Three Steps to Full Visibility</h2>
    <p style="color:#93c5fd;font-size:16px;max-width:500px;margin:0 auto;line-height:1.6;">
      From installed to insight in seconds. No configuration. No learning curve.
    </p>
  </div>

  <div style="display:flex;gap:0;flex-wrap:wrap;align-items:stretch;">

    <!-- Step 1 -->
    <div style="flex:1;min-width:240px;padding:32px 28px;position:relative;">
      <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#0F5586,#6E93B0);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;border:3px solid rgba(255,255,255,0.15);">
        <span style="color:#fff;font-size:26px;font-weight:800;line-height:1;">1</span>
      </div>
      <h3 style="color:#ffffff;font-size:17px;font-weight:800;text-align:center;margin:0 0 14px;">Open Partner Ledger Report</h3>
      <p style="color:#93c5fd;font-size:14px;line-height:1.65;text-align:center;margin:0 0 16px;">
        Navigate to <strong style="color:#bfdbfe;">Accounting &#8250; Reporting &#8250; Partner Ledger</strong>.
        Apply your usual filters — partner, date range, journals. The report looks
        exactly as you know it, now with expand arrows next to each invoice entry.
      </p>
      <div style="background:rgba(15,85,134,0.30);border:1px solid rgba(99,179,237,0.25);border-radius:10px;padding:12px 16px;text-align:center;">
        <span style="color:#fde68a;font-size:12px;font-weight:700;">&#128161; Before: flat list only</span>
      </div>
    </div>

    <!-- Divider arrow -->
    <div style="display:flex;align-items:center;justify-content:center;padding:0 4px;color:rgba(99,179,237,0.40);font-size:28px;flex-shrink:0;">&#8250;</div>

    <!-- Step 2 -->
    <div style="flex:1;min-width:240px;padding:32px 28px;position:relative;">
      <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#0F5586,#6E93B0);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;border:3px solid rgba(255,255,255,0.15);">
        <span style="color:#fff;font-size:26px;font-weight:800;line-height:1;">2</span>
      </div>
      <h3 style="color:#ffffff;font-size:17px;font-weight:800;text-align:center;margin:0 0 14px;">Click Arrow Next to Any Invoice</h3>
      <p style="color:#93c5fd;font-size:14px;line-height:1.65;text-align:center;margin:0 0 16px;">
        Click the <strong style="color:#bfdbfe;">&#9654; expand arrow</strong> to the left of any invoice
        line. The row expands in-place, revealing all its product lines directly below.
        Click again to collapse. Toggle as many invoices as you like simultaneously.
      </p>
      <div style="background:rgba(15,85,134,0.30);border:1px solid rgba(99,179,237,0.25);border-radius:10px;padding:12px 16px;text-align:center;">
        <span style="color:#86efac;font-size:12px;font-weight:700;">&#9654; One-click expand</span>
      </div>
    </div>

    <!-- Divider arrow -->
    <div style="display:flex;align-items:center;justify-content:center;padding:0 4px;color:rgba(99,179,237,0.40);font-size:28px;flex-shrink:0;">&#8250;</div>

    <!-- Step 3 -->
    <div style="flex:1;min-width:240px;padding:32px 28px;">
      <div style="width:64px;height:64px;border-radius:50%;background:linear-gradient(135deg,#0F5586,#6E93B0);display:flex;align-items:center;justify-content:center;margin:0 auto 20px;border:3px solid rgba(255,255,255,0.15);">
        <span style="color:#fff;font-size:26px;font-weight:800;line-height:1;">3</span>
      </div>
      <h3 style="color:#ffffff;font-size:17px;font-weight:800;text-align:center;margin:0 0 14px;">See All Product Lines Instantly</h3>
      <p style="color:#93c5fd;font-size:14px;line-height:1.65;text-align:center;margin:0 0 16px;">
        Each product line displays: <strong style="color:#bfdbfe;">Product Name</strong>,
        <strong style="color:#bfdbfe;">Quantity</strong>, <strong style="color:#bfdbfe;">UoM</strong>,
        and <strong style="color:#bfdbfe;">Line Total</strong> in the balance column.
        Full invoice context — zero navigation, zero extra clicks.
      </p>
      <div style="background:rgba(15,85,134,0.30);border:1px solid rgba(99,179,237,0.25);border-radius:10px;padding:12px 16px;text-align:center;">
        <span style="color:#86efac;font-size:12px;font-weight:700;">&#10003; After: full product detail</span>
      </div>
    </div>

  </div>
</div>


<!-- =====================================================================
     SECTION 5 — LIVE SCREENSHOTS SHOWCASE
     ===================================================================== -->
<div style="margin-bottom:40px;">
  <div style="text-align:center;margin-bottom:36px;">
    <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:6px 20px;font-size:12px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;">Live Screenshots</span>
    <h2 style="font-size:clamp(22px,3.5vw,34px);font-weight:800;color:#041F33;margin:16px 0 8px;letter-spacing:-0.3px;">See It In Action</h2>
    <p style="color:#6E93B0;font-size:16px;max-width:520px;margin:0 auto;line-height:1.6;">
      Real Odoo Enterprise Partner Ledger screens with the drill-down module installed.
    </p>
  </div>

  <div style="display:flex;flex-direction:column;gap:28px;">

    <!-- Screenshot 1 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(4,31,51,0.07);">
      <div style="padding:24px 28px 0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
          <div>
            <h3 style="font-size:18px;font-weight:800;color:#041F33;margin:0 0 4px;">Collapsed Partner Ledger View</h3>
            <p style="color:#6E93B0;font-size:14px;margin:0;line-height:1.5;">
              The standard Partner Ledger with expand arrows added to each invoice row.
              Clean, uncluttered — collapse all rows until you need the detail.
              The expand arrow sits neatly to the left of every invoice entry.
            </p>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;flex-shrink:0;">
            <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Collapsed State</span>
            <span style="background:#dbeafe;color:#1d4ed8;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Default View</span>
            <span style="background:#f0fdf4;color:#166534;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">All Invoices</span>
          </div>
        </div>
      </div>
      <div style="background:#E7EEF3;margin:0 16px 16px;border-radius:12px;overflow:hidden;border:1px solid #d1dce8;">
        <div style="background:#d1dce8;padding:8px 14px;display:flex;align-items:center;gap:7px;">
          <span style="width:11px;height:11px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#28c840;display:inline-block;"></span>
          <span style="color:#6E93B0;font-size:11px;margin-left:8px;">Partner Ledger — Collapsed</span>
        </div>
        <img src="01_partner_ledger_collapsed.png"
             alt="Partner Ledger collapsed view with expand arrows next to invoice rows"
             style="width:100%;display:block;" />
      </div>
    </div>

    <!-- Screenshot 2 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(4,31,51,0.07);">
      <div style="padding:24px 28px 0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
          <div>
            <h3 style="font-size:18px;font-weight:800;color:#041F33;margin:0 0 4px;">Expanded Invoice Lines View</h3>
            <p style="color:#6E93B0;font-size:14px;margin:0;line-height:1.5;">
              After clicking the expand arrow — product lines appear inline below the invoice row.
              Each sub-row shows the product name, quantity, unit of measure, and the individual
              line total in the balance column. Completely native Odoo UI styling.
            </p>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;flex-shrink:0;">
            <span style="background:#f0fdf4;color:#166534;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Expanded State</span>
            <span style="background:#fef9c3;color:#854d0e;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Drill-down Active</span>
            <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Product Lines</span>
          </div>
        </div>
      </div>
      <div style="background:#E7EEF3;margin:0 16px 16px;border-radius:12px;overflow:hidden;border:1px solid #d1dce8;">
        <div style="background:#d1dce8;padding:8px 14px;display:flex;align-items:center;gap:7px;">
          <span style="width:11px;height:11px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#28c840;display:inline-block;"></span>
          <span style="color:#6E93B0;font-size:11px;margin-left:8px;">Partner Ledger — Expanded (drill-down active)</span>
        </div>
        <img src="02_partner_ledger_expanded.png"
             alt="Partner Ledger with expanded invoice showing product lines, quantity, UoM and line totals"
             style="width:100%;display:block;" />
      </div>
    </div>

    <!-- Screenshot 3 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(4,31,51,0.07);">
      <div style="padding:24px 28px 0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
          <div>
            <h3 style="font-size:18px;font-weight:800;color:#041F33;margin:0 0 4px;">Product Lines Detail Close-up</h3>
            <p style="color:#6E93B0;font-size:14px;margin:0;line-height:1.5;">
              Detailed view of the expanded product lines. Notice the indented rows, the
              product name in the description column, the precise quantity and UoM fields,
              and the individual monetary amount. All data comes directly from the invoice line records.
            </p>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;flex-shrink:0;">
            <span style="background:#fdf4ff;color:#7e22ce;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Close-up Detail</span>
            <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Qty + UoM</span>
            <span style="background:#f0fdf4;color:#166534;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Line Total</span>
          </div>
        </div>
      </div>
      <div style="background:#E7EEF3;margin:0 16px 16px;border-radius:12px;overflow:hidden;border:1px solid #d1dce8;">
        <div style="background:#d1dce8;padding:8px 14px;display:flex;align-items:center;gap:7px;">
          <span style="width:11px;height:11px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#28c840;display:inline-block;"></span>
          <span style="color:#6E93B0;font-size:11px;margin-left:8px;">Product Lines Detail — Qty, UoM, Amount</span>
        </div>
        <img src="03_product_lines_detail.png"
             alt="Close-up of expanded product lines showing product name, quantity, unit of measure and line total"
             style="width:100%;display:block;" />
      </div>
    </div>

    <!-- Screenshot 4 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:18px;overflow:hidden;box-shadow:0 4px 24px rgba(4,31,51,0.07);">
      <div style="padding:24px 28px 0;">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:16px;">
          <div>
            <h3 style="font-size:18px;font-weight:800;color:#041F33;margin:0 0 4px;">Full Report Overview</h3>
            <p style="color:#6E93B0;font-size:14px;margin:0;line-height:1.5;">
              A full-page view of the Partner Ledger with multiple partners and
              multiple invoices expanded simultaneously. Shows how the drill-down
              feature scales across a busy ledger with multiple customers or vendors.
            </p>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap;flex-shrink:0;">
            <span style="background:#fff7ed;color:#c2410c;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Full Report</span>
            <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Multi-partner</span>
            <span style="background:#dbeafe;color:#1d4ed8;border-radius:50px;padding:5px 13px;font-size:11px;font-weight:700;">Overview</span>
          </div>
        </div>
      </div>
      <div style="background:#E7EEF3;margin:0 16px 16px;border-radius:12px;overflow:hidden;border:1px solid #d1dce8;">
        <div style="background:#d1dce8;padding:8px 14px;display:flex;align-items:center;gap:7px;">
          <span style="width:11px;height:11px;border-radius:50%;background:#ff5f57;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#febc2e;display:inline-block;"></span>
          <span style="width:11px;height:11px;border-radius:50%;background:#28c840;display:inline-block;"></span>
          <span style="color:#6E93B0;font-size:11px;margin-left:8px;">Report Overview — Multi-partner drill-down</span>
        </div>
        <img src="04_report_overview.png"
             alt="Full partner ledger report overview with multiple expanded invoices across multiple partners"
             style="width:100%;display:block;" />
      </div>
    </div>

  </div>
</div>


<!-- =====================================================================
     SECTION 6 — TECHNICAL SPECS TABLE
     ===================================================================== -->
<div style="margin-bottom:40px;">
  <div style="text-align:center;margin-bottom:36px;">
    <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:6px 20px;font-size:12px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;">Technical Specifications</span>
    <h2 style="font-size:clamp(22px,3.5vw,34px);font-weight:800;color:#041F33;margin:16px 0 8px;letter-spacing:-0.3px;">Module Details</h2>
    <p style="color:#6E93B0;font-size:16px;max-width:500px;margin:0 auto;line-height:1.6;">
      Everything you need to evaluate compatibility before installation.
    </p>
  </div>

  <div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start;">

    <!-- Specs table -->
    <div style="flex:2;min-width:300px;background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;overflow:hidden;">
      <div style="background:linear-gradient(90deg,#041F33,#063153);padding:18px 24px;">
        <span style="color:#ffffff;font-size:15px;font-weight:700;">&#128203; Module Manifest</span>
      </div>
      <table style="width:100%;border-collapse:collapse;">
        <tbody>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;width:38%;background:#fafbfc;">Module Name</td>
            <td style="padding:16px 20px;font-size:14px;font-weight:600;color:#041F33;">COA Partner Ledger Invoice Drill-down</td>
          </tr>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">Technical ID</td>
            <td style="padding:16px 20px;">
              <code style="background:#E7EEF3;color:#0F5586;border-radius:6px;padding:3px 10px;font-size:13px;font-weight:700;">coa_partner_ledger_details</code>
            </td>
          </tr>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">Odoo Versions</td>
            <td style="padding:16px 20px;">
              <span style="background:#dbeafe;color:#1d4ed8;border-radius:6px;padding:3px 10px;font-size:12px;font-weight:700;margin-right:6px;">17.0</span>
              <span style="background:#dbeafe;color:#1d4ed8;border-radius:6px;padding:3px 10px;font-size:12px;font-weight:700;margin-right:6px;">18.0</span>
              <span style="background:#dbeafe;color:#1d4ed8;border-radius:6px;padding:3px 10px;font-size:12px;font-weight:700;">19.0</span>
            </td>
          </tr>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">Edition</td>
            <td style="padding:16px 20px;">
              <span style="background:#fef3c7;color:#92400e;border-radius:6px;padding:3px 10px;font-size:12px;font-weight:700;">&#9733; Enterprise Only</span>
            </td>
          </tr>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">Dependencies</td>
            <td style="padding:16px 20px;">
              <code style="background:#f0fdf4;color:#166534;border-radius:6px;padding:3px 10px;font-size:13px;font-weight:700;border:1px solid #bbf7d0;">account</code>
              &nbsp;
              <code style="background:#fdf4ff;color:#7e22ce;border-radius:6px;padding:3px 10px;font-size:13px;font-weight:700;border:1px solid #e9d5ff;">account_reports</code>
            </td>
          </tr>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">License</td>
            <td style="padding:16px 20px;">
              <span style="background:#E7EEF3;color:#041F33;border-radius:6px;padding:3px 10px;font-size:13px;font-weight:700;">OPL-1</span>
              <span style="color:#6E93B0;font-size:12px;margin-left:8px;">(Odoo Proprietary License v1)</span>
            </td>
          </tr>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">Languages</td>
            <td style="padding:16px 20px;">
              <span style="background:#E7EEF3;color:#041F33;border-radius:6px;padding:3px 10px;font-size:12px;font-weight:700;margin-right:6px;">&#127482;&#127480; English</span>
              <span style="background:#E7EEF3;color:#041F33;border-radius:6px;padding:3px 10px;font-size:12px;font-weight:700;">&#127462;&#127466; Arabic</span>
            </td>
          </tr>
          <tr style="border-bottom:1px solid #E7EEF3;">
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">Author</td>
            <td style="padding:16px 20px;font-size:14px;font-weight:700;color:#041F33;">Code Of Arts (COA)</td>
          </tr>
          <tr>
            <td style="padding:16px 20px;font-size:13px;font-weight:700;color:#6E93B0;text-transform:uppercase;letter-spacing:0.5px;background:#fafbfc;">Website</td>
            <td style="padding:16px 20px;font-size:14px;font-weight:600;color:#0F5586;">https://www.coa-egy.com</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Compatibility + requirements panel -->
    <div style="flex:1;min-width:240px;display:flex;flex-direction:column;gap:18px;">

      <!-- Compatibility card -->
      <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;padding:24px;">
        <div style="font-size:14px;font-weight:800;color:#041F33;margin-bottom:16px;">&#9989; Compatibility Checklist</div>
        <div style="display:flex;flex-direction:column;gap:11px;">
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="width:20px;height:20px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:11px;font-weight:800;">&#10003;</span>
            <span style="font-size:13px;color:#374151;">Odoo 17 Enterprise</span>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="width:20px;height:20px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:11px;font-weight:800;">&#10003;</span>
            <span style="font-size:13px;color:#374151;">Odoo 18 Enterprise</span>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="width:20px;height:20px;border-radius:50%;background:#bbf7d0;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#166534;font-size:11px;font-weight:800;">&#10003;</span>
            <span style="font-size:13px;color:#374151;">Odoo 19 Enterprise</span>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="width:20px;height:20px;border-radius:50%;background:#fecaca;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#8C1D22;font-size:11px;font-weight:800;">&#10005;</span>
            <span style="font-size:13px;color:#6b7280;">Odoo Community (any)</span>
          </div>
          <div style="display:flex;align-items:center;gap:10px;">
            <span style="width:20px;height:20px;border-radius:50%;background:#fecaca;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#8C1D22;font-size:11px;font-weight:800;">&#10005;</span>
            <span style="font-size:13px;color:#6b7280;">Odoo 16 or earlier</span>
          </div>
        </div>
      </div>

      <!-- Requirements card -->
      <div style="background:linear-gradient(135deg,#041F33,#063153);border-radius:16px;padding:24px;">
        <div style="font-size:14px;font-weight:800;color:#ffffff;margin-bottom:14px;">&#9888; Requirements</div>
        <div style="display:flex;flex-direction:column;gap:11px;">
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#fde68a;font-size:14px;margin-top:1px;">&#9654;</span>
            <span style="font-size:13px;color:#93c5fd;line-height:1.5;">Odoo Enterprise subscription required</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#fde68a;font-size:14px;margin-top:1px;">&#9654;</span>
            <span style="font-size:13px;color:#93c5fd;line-height:1.5;"><code style="background:rgba(255,255,255,0.1);border-radius:4px;padding:1px 5px;color:#bfdbfe;">account_reports</code> module must be installed</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#fde68a;font-size:14px;margin-top:1px;">&#9654;</span>
            <span style="font-size:13px;color:#93c5fd;line-height:1.5;">Accounting module (<code style="background:rgba(255,255,255,0.1);border-radius:4px;padding:1px 5px;color:#bfdbfe;">account</code>) active</span>
          </div>
          <div style="display:flex;align-items:flex-start;gap:10px;">
            <span style="color:#fde68a;font-size:14px;margin-top:1px;">&#9654;</span>
            <span style="font-size:13px;color:#93c5fd;line-height:1.5;">No additional configuration needed after install</span>
          </div>
        </div>
      </div>

    </div>
  </div>
</div>


<!-- =====================================================================
     SECTION 7 — FAQ
     ===================================================================== -->
<div style="margin-bottom:40px;">
  <div style="text-align:center;margin-bottom:36px;">
    <span style="background:#E7EEF3;color:#0F5586;border-radius:50px;padding:6px 20px;font-size:12px;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;">FAQ</span>
    <h2 style="font-size:clamp(22px,3.5vw,34px);font-weight:800;color:#041F33;margin:16px 0 8px;letter-spacing:-0.3px;">Frequently Asked Questions</h2>
    <p style="color:#6E93B0;font-size:16px;max-width:500px;margin:0 auto;line-height:1.6;">
      Answers to the most common pre-purchase questions.
    </p>
  </div>

  <div style="display:flex;flex-direction:column;gap:16px;">

    <!-- FAQ 1 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;overflow:hidden;">
      <div style="background:linear-gradient(90deg,#041F33 0%,#063153 100%);padding:20px 24px;display:flex;align-items:center;gap:14px;">
        <div style="width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="color:#93c5fd;font-size:15px;font-weight:800;">Q</span>
        </div>
        <span style="color:#ffffff;font-size:16px;font-weight:700;">Does it work on Odoo Community Edition?</span>
      </div>
      <div style="padding:24px;display:flex;gap:14px;align-items:flex-start;">
        <div style="width:36px;height:36px;border-radius:50%;background:#E7EEF3;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
          <span style="color:#0F5586;font-size:15px;font-weight:800;">A</span>
        </div>
        <div>
          <p style="color:#374151;font-size:15px;line-height:1.7;margin:0 0 12px;">
            <strong style="color:#8C1D22;">No.</strong> This module is built exclusively for <strong>Odoo Enterprise Edition</strong>.
            It extends the <code style="background:#E7EEF3;border-radius:4px;padding:1px 6px;font-size:13px;color:#0F5586;">account_reports</code> module,
            which is an Enterprise-only component. Odoo Community does not include this module,
            so the drill-down functionality cannot be provided on Community.
          </p>
          <div style="background:#fff5f5;border-left:4px solid #E61B21;border-radius:0 8px 8px 0;padding:12px 16px;">
            <span style="color:#8C1D22;font-size:13px;font-weight:600;">&#9888; Requires: Odoo Enterprise 17, 18, or 19 + account_reports</span>
          </div>
        </div>
      </div>
    </div>

    <!-- FAQ 2 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;overflow:hidden;">
      <div style="background:linear-gradient(90deg,#041F33 0%,#063153 100%);padding:20px 24px;display:flex;align-items:center;gap:14px;">
        <div style="width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="color:#93c5fd;font-size:15px;font-weight:800;">Q</span>
        </div>
        <span style="color:#ffffff;font-size:16px;font-weight:700;">Will it break after Odoo updates?</span>
      </div>
      <div style="padding:24px;display:flex;gap:14px;align-items:flex-start;">
        <div style="width:36px;height:36px;border-radius:50%;background:#E7EEF3;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
          <span style="color:#0F5586;font-size:15px;font-weight:800;">A</span>
        </div>
        <div>
          <p style="color:#374151;font-size:15px;line-height:1.7;margin:0 0 12px;">
            This module is built using <strong>Odoo's official report extension framework</strong> —
            not template overrides or monkey-patching that are known to break on updates.
            By following the canonical <code style="background:#E7EEF3;border-radius:4px;padding:1px 6px;font-size:13px;color:#0F5586;">account_reports</code> API,
            the module stays aligned with Odoo's own upgrade path.
          </p>
          <p style="color:#374151;font-size:15px;line-height:1.7;margin:0 0 12px;">
            Code Of Arts actively maintains and tests the module against each new
            Odoo version as it is released. We publish updated versions for 17, 18, and 19
            simultaneously. When Odoo 20 ships, an updated version will follow.
          </p>
          <div style="background:#f0fdf4;border-left:4px solid #22c55e;border-radius:0 8px 8px 0;padding:12px 16px;">
            <span style="color:#166534;font-size:13px;font-weight:600;">&#10003; Actively maintained across all supported Odoo Enterprise versions</span>
          </div>
        </div>
      </div>
    </div>

    <!-- FAQ 3 -->
    <div style="background:#ffffff;border:1.5px solid #E7EEF3;border-radius:16px;overflow:hidden;">
      <div style="background:linear-gradient(90deg,#041F33 0%,#063153 100%);padding:20px 24px;display:flex;align-items:center;gap:14px;">
        <div style="width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.12);border:1.5px solid rgba(255,255,255,0.25);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
          <span style="color:#93c5fd;font-size:15px;font-weight:800;">Q</span>
        </div>
        <span style="color:#ffffff;font-size:16px;font-weight:700;">Can I see subtotals by product across multiple invoices?</span>
      </div>
      <div style="padding:24px;display:flex;gap:14px;align-items:flex-start;">
        <div style="width:36px;height:36px;border-radius:50%;background:#E7EEF3;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;">
          <span style="color:#0F5586;font-size:15px;font-weight:800;">A</span>
        </div>
        <div>
          <p style="color:#374151;font-size:15px;line-height:1.7;margin:0 0 12px;">
            The current version of this module focuses on <strong>per-invoice drill-down</strong>:
            expanding a single invoice row to see its individual product lines, each with
            its quantity, UoM, and line total. Cross-invoice product subtotals (e.g., total
            quantity of Product X across all invoices for a partner) are not aggregated in
            the current release.
          </p>
          <p style="color:#374151;font-size:15px;line-height:1.7;margin:0 0 12px;">
            For cross-invoice product analysis, Odoo's native <strong>Sales Analysis</strong> or
            <strong>Purchase Analysis</strong> reports, or a custom pivot view, would be the
            appropriate tool. This module is purpose-built for ledger-level invoice drill-down
            in the accounting context.
          </p>
          <div style="background:#E7EEF3;border-left:4px solid #0F5586;border-radius:0 8px 8px 0;padding:12px 16px;">
            <span style="color:#0F5586;font-size:13px;font-weight:600;">&#128161; Tip: Use Sales/Purchase Analysis reports for cross-invoice product aggregation</span>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>


<!-- =====================================================================
     SECTION 8 — FOOTER CTA
     ===================================================================== -->
<div style="background:linear-gradient(135deg,#041F33 0%,#063153 55%,#0F5586 100%);border-radius:18px;padding:56px 48px;text-align:center;position:relative;overflow:hidden;">
  <div style="position:absolute;top:-50px;right:-50px;width:280px;height:280px;border-radius:50%;background:rgba(15,85,134,0.22);pointer-events:none;"></div>
  <div style="position:absolute;bottom:-70px;left:-30px;width:240px;height:240px;border-radius:50%;background:rgba(6,49,83,0.35);pointer-events:none;"></div>

  <!-- Logo -->
  <div style="display:inline-flex;align-items:center;justify-content:center;gap:12px;margin-bottom:28px;">
    <img src="coa_logo.jpg" alt="Code Of Arts Logo"
         style="width:64px;height:64px;border-radius:50%;object-fit:cover;border:3px solid rgba(255,255,255,0.25);box-shadow:0 8px 32px rgba(0,0,0,0.3);" />
    <div style="text-align:left;">
      <div style="color:#ffffff;font-size:20px;font-weight:800;letter-spacing:0.3px;">Code Of Arts</div>
      <div style="color:#93c5fd;font-size:13px;font-weight:500;margin-top:2px;">Enterprise Odoo Solutions</div>
    </div>
  </div>

  <h2 style="color:#ffffff;font-size:clamp(22px,3.5vw,36px);font-weight:800;margin:0 0 16px;letter-spacing:-0.3px;">
    Ready to See Every Invoice Line?
  </h2>
  <p style="color:#bfdbfe;font-size:17px;line-height:1.65;max-width:560px;margin:0 auto 36px;">
    Install <strong style="color:#ffffff;">COA Partner Ledger Invoice Drill-down</strong> today
    and give your accounting team the product-level visibility they deserve —
    without leaving the Partner Ledger.
  </p>

  <!-- Contact info cards -->
  <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-bottom:36px;">
    <div style="background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.20);border-radius:14px;padding:18px 28px;min-width:200px;">
      <div style="color:#93c5fd;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">&#128231; Support Email</div>
      <a href="mailto:info@coa-egy.com" style="color:#ffffff;font-size:15px;font-weight:700;text-decoration:none;letter-spacing:0.2px;">info@coa-egy.com</a>
    </div>
    <div style="background:rgba(255,255,255,0.10);border:1px solid rgba(255,255,255,0.20);border-radius:14px;padding:18px 28px;min-width:200px;">
      <div style="color:#93c5fd;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">&#127760; Website</div>
      <a href="https://www.coa-egy.com" style="color:#ffffff;font-size:15px;font-weight:700;text-decoration:none;letter-spacing:0.2px;">www.coa-egy.com</a>
    </div>
  </div>

  <!-- Module tag line -->
  <div style="display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;">
    <span style="background:rgba(99,179,237,0.15);border:1px solid rgba(99,179,237,0.30);color:#93c5fd;border-radius:50px;padding:7px 18px;font-size:12px;font-weight:700;letter-spacing:0.5px;">&#9654; Drill-down</span>
    <span style="background:rgba(99,179,237,0.15);border:1px solid rgba(99,179,237,0.30);color:#93c5fd;border-radius:50px;padding:7px 18px;font-size:12px;font-weight:700;letter-spacing:0.5px;">&#128230; Product Lines</span>
    <span style="background:rgba(99,179,237,0.15);border:1px solid rgba(99,179,237,0.30);color:#93c5fd;border-radius:50px;padding:7px 18px;font-size:12px;font-weight:700;letter-spacing:0.5px;">&#9878; Partner Ledger</span>
    <span style="background:rgba(99,179,237,0.15);border:1px solid rgba(99,179,237,0.30);color:#93c5fd;border-radius:50px;padding:7px 18px;font-size:12px;font-weight:700;letter-spacing:0.5px;">&#9989; v17 · v18 · v19</span>
    <span style="background:rgba(99,179,237,0.15);border:1px solid rgba(99,179,237,0.30);color:#93c5fd;border-radius:50px;padding:7px 18px;font-size:12px;font-weight:700;letter-spacing:0.5px;">&#9881; Enterprise Native</span>
  </div>

  <!-- Copyright -->
  <div style="margin-top:36px;padding-top:24px;border-top:1px solid rgba(255,255,255,0.12);">
    <p style="color:rgba(255,255,255,0.45);font-size:13px;margin:0;">
      &copy; 2024 Code Of Arts (COA). All rights reserved.
      &nbsp;|&nbsp; License: OPL-1
      &nbsp;|&nbsp; <a href="https://www.coa-egy.com" style="color:rgba(255,255,255,0.55);text-decoration:none;">www.coa-egy.com</a>
    </p>
  </div>
</div>

</div>"""

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"File written: {OUTPUT_PATH}")

import os
size = os.path.getsize(OUTPUT_PATH)
print(f"File size: {size:,} bytes")

# Verify no BOM
with open(OUTPUT_PATH, 'rb') as f:
    first_bytes = f.read(4)
print(f"First 4 raw bytes (hex): {first_bytes.hex()}")
has_bom = first_bytes[:3] == b'\xef\xbb\xbf'
print(f"BOM present: {has_bom}")

# Print first 5 text lines
with open(OUTPUT_PATH, 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f"\nTotal lines: {len(lines)}")
print("\nFirst 5 lines:")
for i, line in enumerate(lines[:5], 1):
    print(f"  [{i}] {repr(line[:120])}")
"""

with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(HTML)
