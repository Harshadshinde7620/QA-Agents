# Design System Specification: The Intelligence Architect

## 1. Overview & Creative North Star
**Creative North Star: "The Digital Curator"**

In the world of B2B AI, data is often chaotic. This design system is not a mere "dashboard"; it is an editorial lens that brings order to information. We move away from the "industrial" feel of traditional B2B tools toward a high-end, curated experience. 

The aesthetic is defined by **Atmospheric Depth** and **Intentional Asymmetry**. Instead of a rigid, boxed-in grid, we use expansive white space and "The Layering Principle" to create a sense of calm authority. By utilizing sophisticated tonal shifts rather than harsh lines, the interface feels fluid, intelligent, and premium.

---

## 2. Colors & Surface Philosophy

The palette is rooted in deep, authoritative teals and cool neutrals, designed to reduce cognitive load while maintaining a professional "SaaS-Elite" edge.

### The "No-Line" Rule
To achieve a signature high-end look, **1px solid borders for sectioning are strictly prohibited.** Layout boundaries must be defined solely through background shifts. 
- *Implementation:* Place a `surface-container-lowest` card on a `surface` background to define its shape.

### Surface Hierarchy & Nesting
Treat the UI as a series of physical layers—like stacked sheets of fine paper.
- **Level 0 (Base):** `surface` (#f7fafb) - The expansive canvas.
- **Level 1 (Sections):** `surface-container-low` (#f2f4f5) - Used for sidebars or secondary panels.
- **Level 2 (Interaction):** `surface-container` (#eceef0) - The default for content modules.
- **Level 3 (Focus):** `surface-container-highest` (#e0e3e4) - Used for active states or highlighted data.

### The "Glass & Gradient" Rule
For primary actions and floating elements, use:
- **Glassmorphism:** Apply `surface` with 70% opacity and a 12px backdrop-blur.
- **Signature Textures:** Main CTAs should use a subtle linear gradient (45°) from `primary` (#004655) to `primary_container` (#005f73). This provides a "visual soul" that flat colors lack.

---

## 3. Typography: Editorial Authority

We use a dual-sans-serif approach to balance character with utility.

*   **Display & Headlines (Manrope):** Chosen for its geometric precision and modern "tech-forward" personality. Use `headline-lg` and `headline-md` with tighter letter-spacing (-0.02em) to create an authoritative, editorial header feel.
*   **Body & Labels (Inter):** The industry standard for legibility. Inter handles the dense data of review management with ease.

**Hierarchy as Identity:**
- **Primary Data Points:** Use `title-lg` in `on_surface` for review scores or AI sentiment percentages.
- **Metadata:** Use `label-md` in `on_surface_variant` for timestamps and source tags.

---

## 4. Elevation & Depth

We eschew traditional "drop shadows" in favor of **Tonal Layering**.

### The Layering Principle
Depth is achieved by stacking tiers. An inner container should always be at least one tier "Higher" or "Lower" than its parent. This creates a soft, natural lift without visual noise.

### Ambient Shadows
When a component must "float" (e.g., a dropdown or modal):
- **Shadow Color:** Use a tinted version of `on_surface` (e.g., #191c1d at 6% opacity).
- **Blur:** Minimum 24px. The goal is an "ambient glow" rather than a hard edge.

### The "Ghost Border" Fallback
If contrast is legally required for accessibility:
- Use `outline_variant` at **15% opacity**. Never use 100% opaque borders.

---

## 5. Components

### Buttons
- **Primary:** Gradient fill (`primary` to `primary_container`), `on_primary` text. Border radius: `md` (0.375rem).
- **Secondary:** `surface_container_highest` fill, `on_surface` text. No border.
- **Tertiary:** Transparent background, `primary` text. Use only for low-emphasis actions.

### Cards & Lists
- **Rule:** Forbid divider lines.
- **Execution:** Separate reviews in a list by using a `sm` (24px) vertical spacing gap. Use a subtle background change (`surface_container_lowest`) on hover to indicate interactivity.

### Input Fields
- **Default State:** `surface_container_low` background with a `Ghost Border`.
- **Focus State:** Background remains, but the `outline` token is applied at 100% opacity to create a sharp, intentional focus ring.

### AI Sentiment Chips
- **Positive:** `secondary_container` background with `on_secondary_fixed_variant` text.
- **Negative:** `error_container` background with `on_error_container` text.
- **Design Note:** Use `full` roundedness (9999px) for chips to contrast against the `md` roundedness of the main containers.

### Review Sentiment Visualizer (Custom Component)
Instead of a standard bar chart, use a "Tonal Pulse": A wide, low-profile component using `primary_fixed` as a background with a `primary` "pulse" indicator that uses a subtle glow (ambient shadow) to show AI-detected trends.

---

## 6. Do's and Don'ts

### Do
- **Do** use white space as a structural element. If a design feels crowded, increase padding rather than adding a divider.
- **Do** use `tertiary` (#603401) sparingly for "AI Insights" or "Action Required" highlights to provide a sophisticated warm contrast to the teals.
- **Do** ensure all interactive elements have a clear `surface_container_highest` hover state.

### Don't
- **Don't** use pure black (#000000) for text. Always use `on_surface` (#191c1d) to maintain the premium, soft-contrast feel.
- **Don't** use the `DEFAULT` (0.25rem) corner radius for large containers; reserve it for small inputs. Use `xl` (0.75rem) for main dashboard cards to feel "Contemporary."
- **Don't** use standard "12-column" grids that feel boxed in. Allow elements to bleed to the edges of their containers to create an expansive, modern layout.