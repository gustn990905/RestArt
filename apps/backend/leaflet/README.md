Set-Content -Encoding UTF8 -Path "apps/backend/leaflet/README.md" -Value @'

# Mobile Leaflet Feature

This directory documents the mobile leaflet feature implemented in the RestArt backend prototype.

The mobile leaflet feature generates a personalized leaflet result from a user-provided exhibition image. It connects image matching, color extraction, artwork recommendation, exhibition recommendation, and leaflet design selection into one service flow.

## Feature Role

The mobile leaflet feature is used when a visitor interacts with artworks or exhibition images and receives a personalized leaflet-style result.

The feature is different from the space-based artwork recommendation flow.

| Feature                            | Main Input                  | Main Purpose                           |
| ---------------------------------- | --------------------------- | -------------------------------------- |
| Mobile Leaflet                     | Exhibition or artwork image | Generate a personalized leaflet result |
| Space-based Artwork Recommendation | Interior or space image     | Recommend artworks that match a space  |

## Related Backend Endpoint

The original backend prototype includes the following endpoint:

```text
POST /leaflet_creating/
```
