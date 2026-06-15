Set-Content -Encoding UTF8 -Path "docs/12-mobile-leaflet/mobile-leaflet-flow.md" -Value @'

# Mobile Leaflet Flow

This document describes the mobile leaflet generation flow in the RestArt backend prototype.

The mobile leaflet feature creates a personalized leaflet-style result from a user-provided exhibition or artwork image. It combines image matching, color analysis, artwork recommendation, exhibition connection, and leaflet design selection.

## Feature Purpose

The mobile leaflet feature is designed for an exhibition experience.

A visitor can use an image related to an artwork or exhibition, and the system generates a personalized leaflet result based on visual similarity, representative colors, and recommendation logic.

## Related Endpoint

```text
POST /leaflet_creating/
```
