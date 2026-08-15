# Copy-Edit Log — Markdown

Tracks copy-editing passes over this module's `.qmd` documents. Clear-cut
typos/grammar/spelling errors are corrected directly in the source. Items
that need an author decision are left in place but wrapped in
`<mark>...</mark>` so they show up highlighted in the rendered HTML.

## narrative.qmd — 2026-08-15

### Fixed directly (typos, spelling, grammar)

| Line | Issue | Fix |
|---|---|---|
| 14 | "interpreation", "effecient", "reproducibaility" | "interpretation", "efficient", "reproducibility" |
| 34 | "it can replaced with" (missing "be") | "it can be replaced with" |
| 46 | "a analysis" | "an analysis" |
| 65 | "reserach manuscript" | "research manuscript" |
| 96 | "novel approch" | "novel approach" |
| 97 | "genetic connetivity" | "genetic connectivity" |
| 111 | "title, keywords, fundin, and abstract" | "funding" |
| 134 | "What Markdown does is allows you" (pseudo-cleft needs bare infinitive) | "is allow you" |
| 166 | "So the markdown." before a code example | "So the markdown:" |
| 208 | "### FootNotes" (inconsistent heading case) | "### Footnotes" |
| 212 | "jumpt to the bottom" | "jump to the bottom" |
| 216 | `[^1]:. This is...` (stray period) | `[^1]: This is...` |
| 227 | "On of the strengths" | "One of the strengths" |
| 227 | "copy-and-paste it togehter" | "together" |
| 233 | "three acute accents (back ticks)" — contradicts the very next sentence, which correctly calls the character "grave" | "three grave accents (back ticks)" |
| 238 | "a chunck" | "a chunk" |
| 259 | "all the chuncks" | "all the chunks" |
| 268 | "show its contentws" | "contents" |
| 288 | "with all my chunks showing" (missing terminal period) | added period |
| 307 | "render/preview the document the document" (duplicated) | "render/preview the document" |
| 307 | "your anlayses" (in an aside note) | "your analyses" |
| 307 | stray period after `{.aside}` (doubled terminal punctuation) | removed |
| ~162 | dangling empty `\| ` row at the end of the Markdown-syntax table | removed |

### Flagged for your review (highlighted with `<mark>` in the source)

| Line | Text | Why it's flagged |
|---|---|---|
| ~104 | "populations of X and another is applied to an analysis of" (inside the quoted manuscript abstract) | Breaks parallel structure with "one evaluating..." earlier in the sentence. This is your own quoted abstract text, so I didn't rewrite your research wording — worth a look if you want it copy-tight. |
| ~154 | "I find it much easier to just put the" | Sentence cuts off right before the Markdown-syntax table — looks like the rest of the thought never got typed. |
| ~307 | "When you render/preview the document, it will be run and the contents between these symbols and replaced the content by the output of the `R` code itself." | Still doesn't fully parse after removing the duplicate "the document" — likely missing "are" ("...the contents...are replaced...") and/or "with" instead of "by". Left for you to finish since there are a few ways to fix it. |
