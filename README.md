[🇮🇷 نسخه فارسی](README.fa.md)

# Textile Calculator — Python / Tkinter

> ⚠️ **This repository is archived.**
> This version is no longer maintained. Please use the web version instead:
> **[https://calc.parsianik.com/](https://calc.parsianik.com/)** *(replace with your actual Cloudflare Pages URL)*

---

## About

Textile Calculator is a desktop calculation tool for the textile manufacturing industry, developed by **Parsianik Group**. This version is built with Python and the Tkinter GUI library. It covers 15 formulas across 4 core production process categories spanning yarn and fabric manufacturing.

---

## Categories & Formulas

### 1. Melt Spinning (ذوب ریسی)
| Formula | Inputs |
|---|---|
| Theoretical production weight per minute | Speed, number of yarn ends, denier count |
| Theoretical production weight over active time | Theoretical weight/min, machine runtime |
| Theoretical weight of produced product | Masterbatch %, chip weight, oil % |
| Theoretical number of full bobbins | Theoretical product weight, full bobbin weight |
| Total waste weight | Fixed waste, line waste weight |
| Production efficiency | Actual final product weight, theoretical weight over active time |

### 2. Texturing (تکسچره)
| Formula | Inputs |
|---|---|
| Theoretical production weight (kg) | Number of positions, production time, production speed, output yarn count |
| Output yarn count (denier) | Input yarn count, draw ratio, oil %, feed draw %, draw count |
| Production efficiency (%) | Actual yarn produced, theoretical production weight |
| Quality efficiency (%) | Actual yarn produced, off-grade yarn produced |

### 3. Twisting (تابندگی)
| Formula | Inputs |
|---|---|
| Twists per meter | Take-up speed, twister speed |
| Output yarn count | Input yarn count, twists per meter |

### 4. Weaving (بافندگی)
| Formula | Inputs |
|---|---|
| Fabric areal density (g/m²) | Weft density, warp count, weft count, warp density |
| Weight per linear meter (g/m) | Width, areal density |
| Number of warp beam yarn ends | Creel capacity, total yarn ends |

---

## Requirements

- Python 3.x
- Tkinter (included in most standard Python installations)

---

## How to Run

```bash
python formula_calculator_categ.py
```

---

## Project Structure

```
textile-calculator-python/
│
├── formula_calculator_categ.py   # Main application file
└── README.md
```

---

## Why Archived?

This version was designed for desktop systems and required a local Python installation. The web version replaces it with no installation required — it runs in any browser on any device including mobile phones and tablets, and can be embedded directly in a website.

| | Python Version | Web Version |
|---|---|---|
| Requires installation | ✅ Python + Tkinter | ❌ None |
| Mobile compatible | ❌ | ✅ |
| Embeddable in a website | ❌ | ✅ |
| Easy to update | Limited | ✅ |

---

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## Developer

Parsianik Group
