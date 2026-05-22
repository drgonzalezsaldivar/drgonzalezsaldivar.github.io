# Landing Page Report — drgonzalezsaldivar.com
**Page**: `index.html` | **Date**: 2026-04-06 | **Size**: 1.7MB / 1,850 lines

---

## Score Summary

```
Message Match:    ██████████  90/100  ✓
Mobile:           █████████░  90/100  ✓
WhatsApp CTAs:    ██████████  100/100 ✓
Trust Signals:    ████████░░  80/100  ✓
Heading/SEO:      ████████░░  80/100  ✓
Schema:           █████░░░░░  50/100  ⚠
Page Speed:       ██████░░░░  60/100  ⚠
Conversion Track: ██░░░░░░░░  20/100  ❌
─────────────────────────────────────────
Campaign Ready:   ████░░░░░░  40/100  ❌
```

**Campaign readiness is blocked by unconfigurated tracking pixels.**

---

## 🚨 CRITICAL — Fix Before Running Any Ads

### 1. Meta Pixel NOT Active
- **File location**: line ~685
- **Current code**: `fbq('init', 'TU_PIXEL_ID')` — literal placeholder
- **Impact**: Zero Meta conversion data, no remarketing audiences, no ROAS calculation
- **Fix**: Replace `TU_PIXEL_ID` with your real Meta Pixel ID from Events Manager

### 2. Google Tag NOT Active
- **File location**: line ~699
- **Current code**: `G-XXXXXXXXXX` — literal placeholder
- **Impact**: Google Ads cannot optimize bids, no GA4 data, no conversion tracking
- **Fix**: Replace `G-XXXXXXXXXX` with your real GA4 Measurement ID

### 3. No UTM Parameters on Any CTA Link
- **Current**: All 13 WhatsApp links use a static message with no tracking parameters
- **Impact**: Cannot tell which ad, keyword, or campaign drives appointments
- **Fix**: Add UTM params per channel:
  ```
  https://wa.me/528126555222?text=Hola...&utm_source=google&utm_medium=cpc&utm_campaign=ortopedista-monterrey
  ```

---

## ⚠ HIGH — Fix Before Scaling Budget

### 4. Missing LocalBusiness Schema (JSON-LD)
- FAQPage schema is correctly implemented (5 Q&As, rich result eligible)
- But no `LocalBusiness` / `MedicalBusiness` schema for address, phone, hours
- No `AggregateRating` schema — 18 five-star reviews are not surfaced in Google SERPs
- **Fix**: Add these two blocks after the existing FAQPage JSON-LD:

```json
{
  "@context": "https://schema.org",
  "@type": "Physician",
  "name": "Dr. Juan Carlos González Saldívar",
  "description": "Ortopedista Oncológico en Monterrey",
  "url": "https://www.drgonzalezsaldivar.com/",
  "telephone": "+528183877237",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Av. Eugenio Garza Sada 3551, Local D-13",
    "addressLocality": "Monterrey",
    "addressRegion": "Nuevo León",
    "postalCode": "64860",
    "addressCountry": "MX"
  },
  "openingHours": ["Mo-Fr 10:00-19:30", "Sa 10:00-13:00"],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5",
    "reviewCount": "18"
  }
}
```

### 5. No GA4 Conversion Events Defined
- No custom events for WhatsApp click, phone call click, or page scroll
- Without events, Google Ads Smart Bidding has nothing to optimize toward
- **Fix**: After activating GA4, add click-event triggers for `.wa-float` and all `wa.me` links

### 6. Page Size: 1.7MB
- Heavy inline CSS (1,000+ `style=` attributes) cannot be cached by browser
- No image lazy loading detected below the fold
- No WebP/AVIF format references found
- **Impact**: ~7% CVR drop per second of delay; especially critical for Meta mobile traffic
- **Fix priority**: Compress images first (highest gain), then extract CSS to external file

---

## ✓ STRENGTHS — What's Working Well

| Element | Detail |
|---------|--------|
| **WhatsApp CTAs** | 13 strategic placements: hero, floating button, FAQ, contact, blog, services |
| **Message match** | Hero H1 + tagline directly match orthopedic + oncology search intent |
| **Mobile layout** | Full responsive with hamburger nav, stacked columns, 48px tap targets |
| **Phone link** | `tel:+528183877237` correctly formatted — one-tap call on mobile |
| **Trust signals** | 18 Google reviews (all 5★), license numbers (9481533 / 12293070), Christus Muguerza affiliation |
| **FAQ schema** | 5 Q&As live (cost, insurance, hours, location, tumors) — eligible for Google rich results |
| **Business hours** | Visible above the fold + in FAQ schema |
| **Insurance coverage** | MetLife, AXA, Mapfre, BX+ named explicitly — reduces friction for insured patients |
| **Keyword density** | "Monterrey" 30+ mentions, "Plaza Contry" 6+, clinical terms well distributed |

---

## Message Match Analysis (Ad → Page)

| Ad Target Keyword | Landing Page Match | Score |
|---|---|---|
| "Ortopedista oncológico Monterrey" | H1 name + "Oncología" pill + Meta title | **100%** |
| "Dolor de rodilla Monterrey" | Hero copy mentions rodilla; H3 service "Desgaste Articular" | **80%** |
| "Tumor óseo Monterrey" | H3 "Tumores Musculoesqueléticos" + oncology credentials | **90%** |
| "Ortopedista Plaza Contry" | "Plaza Contry" in hero tagline, address, multiple sections | **100%** |
| "Biopsia ósea Nuevo León" | Not found in visible page content | **20%** ⚠ |

**Action**: Add "biopsia ósea" to the Tumores Musculoesqueléticos service card if running ads for that keyword.

---

## Quick Wins by Conversion Impact

| Priority | Action | Effort | CVR Impact |
|---|---|---|---|
| 1 | Activate Meta Pixel (real ID) | 5 min | Unlocks all Meta optimization |
| 2 | Activate Google Tag (real ID) | 5 min | Unlocks Smart Bidding |
| 3 | Add UTM params to hero WhatsApp CTA | 10 min | Attribution clarity |
| 4 | Add AggregateRating schema | 20 min | Star rating in SERPs → higher CTR |
| 5 | Add LocalBusiness/Physician schema | 30 min | Local pack eligibility |
| 6 | Compress hero image to WebP | 15 min | Faster LCP → better CVR on mobile |
| 7 | Add `loading="lazy"` to below-fold images | 10 min | Faster TTI |
| 8 | Add "biopsia ósea" to tumores service card | 10 min | Message match for oncology ads |

---

## Platform Notes

| Platform | Status | Notes |
|---|---|---|
| **Google Ads** | ❌ Not ready | Tag placeholder, no conversion events |
| **Meta Ads** | ❌ Not ready | Pixel placeholder, domain verification needed |
| **Mobile (TikTok/IG)** | ✓ Page ready | Excellent mobile layout, WhatsApp flow works |
| **Desktop (Microsoft)** | ✓ Page ready | Desktop layout strong, trust signals visible |

