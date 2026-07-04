<a name="readme-top"></a>

[![HASSFEST](https://github.com/ngocjohn/lunar-phase/actions/workflows/hassfest.yaml/badge.svg)](https://github.com/ngocjohn/lunar-phase/actions/workflows/hassfest.yaml) ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/ngocjohn/lunar-phase/total?style=flat&logo=homeassistantcommunitystore&logoSize=auto&label=Downloads&color=%2318BCF2) ![GitHub Downloads (all assets, latest release)](https://img.shields.io/github/downloads/ngocjohn/lunar-phase/latest/total?style=flat&logo=homeassistantcommunitystore&logoSize=auto)

# 🌘 Lunar Phase Integration for Home Assistant

<img src="https://raw.githubusercontent.com/ngocjohn/lunar-phase/main/assets/lunar-header.gif" style="border-radius: 8px" />

##

<p style="text-align: justify;">The Lunar Phase integration is a custom component for Home Assistant that provides detailed information about the current phase of the moon. This integration leverages precise astronomical calculations to deliver accurate lunar data, making it a valuable addition for those interested in astronomy, astrology, or just tracking the moon's phases.</p>

## Features

- **Current Moon Phase**: Displays the current phase of the moon.
- **Moon Age**: Shows the age of the moon in days.
- **Distance to Moon**: Provides the distance to the moon in kilometers.
- **Illumination Fraction**: Indicates the fraction of the moon that is illuminated.
- **Moon Illuminance**: Estimated moonlight illuminance in lux (Krisciunas-Schaefer model).
- **Moon Rise and Set Times**: Displays the moon rise and set times.
- **Next Key Phases**: Provides the date and time of the next new moon, full moon, first quarter, and third quarter.
- **Moon Position**: Provides altitude, azimuth, and parallactic angle of the moon.
- **Next Moon High**: Indicates the time of the next moon high position.

  <img src="https://raw.githubusercontent.com/ngocjohn/lunar-phase/main/assets/lunar-entities.png" alt="Lunar Phase Entities">
  <img src="https://raw.githubusercontent.com/ngocjohn/lunar-phase/main/assets/lunar-phase.png" alt="Lunar Phase Sensor Attributes">

## Enhance Your Dashboard with a Beautiful Lunar Display

> [!TIP]
> If you're looking to add a visually appealing and informative lunar phase tracker to your Home Assistant dashboard, check out my custom Lunar Phase Card. This card provides detailed Moon phases information and integrates seamlessly with your existing setup. It's a great addition for anyone interested in astronomy or simply wanting to keep track of the moon's phases in a stylish way. You can find and install the Lunar Phase Card [here](https://github.com/ngocjohn/lunar-phase-card/).

<div style="display: flex; justify-content: space-around;">
  <img src="https://raw.githubusercontent.com/ngocjohn/lunar-phase/main/assets/lunar-default.png" alt="Lunar Phase Cards" width="48%" height="100%">
  <img src="https://raw.githubusercontent.com/ngocjohn/lunar-phase/main/assets/lunar-compact.png" alt="Lunar Phase Calendar" width="48%" height="100%">
</div>

## Table of contents

<details>
    <summary>Table of contents</summary>

- [Features](#features)
- [Installation](#installation)
  - [HACS Installation](#hacs-installation)
  - [Manual Installation](#manual-installation)
- [Configuration](#configuration)
  - [Using the Home Assistant UI](#using-the-home-assistant-ui)
- [Sensor Details](#sensor-details)
- [Contribution](#contribution)

</details>

## Installation

### HACS Installation

1. Go to the HACS settings and add this repository as a custom repository.
2. Search for "Lunar Phase" in HACS and install it.
3. Restart Home Assistant.

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ngocjohn&repository=lunar-phase&category=Integration)

### Manual Installation

1. Download the `lunar_phase` folder from this repository.
2. Copy the `lunar_phase` folder to your Home Assistant `custom_components` directory. The `custom_components` directory resides in the same directory as your `configuration.yaml` file.
3. Restart Home Assistant.

## Configuration

### Using the Home Assistant UI

To configure the Lunar Phase integration, follow these steps:

1. Go to the Home Assistant dashboard.
2. Navigate to `Configuration` > `Devices & Services` > `Add Integration`.
3. Search for `Lunar Phase` and select it.
4. A single form appears pre-filled with your HA home location details. Edit any field if needed, then submit:
   - **Location Name** — defaults to your HA `location_name`, free-text label.
   - **Latitude** — pre-filled from your HA home coordinates, editable.
   - **Longitude** — pre-filled from your HA home coordinates, editable.

   Region and timezone are inferred automatically from HA settings and are not shown.

Once configured, the integration will add the Moon Phase sensor along with other diagnostic sensors that provide detailed lunar information.

## Sensor Details

| **Name**                         | **Description**                                                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------------- |
| `Moon Phase`                     | Displays the current phase of the moon (e.g., New Moon, Waxing Crescent, First Quarter, etc.). |
| `Moon Age`                       | Shows the age of the moon in days.                                                             |
| `Moon Distance`                  | Provides the distance to the moon in kilometers.                                               |
| `Moon Illumination Fraction`     | Indicates the fraction of the moon that is illuminated.                                        |
| `Moon Illuminance`               | Estimated moonlight illuminance in lux; returns 0.0 when moon is below the horizon.           |
| `Moon Rise`                      | Displays the time of the next moonrise.                                                        |
| `Moon Set`                       | Displays the time of the next moonset.                                                         |
| `Moon High`                      | Provides the time of the next moon high position.                                              |
| `Next Full Moon`                 | Provides the date for the next full moon.                                                      |
| `Next New Moon`                  | Provides the date for the next new moon.                                                       |
| `Next Third Quarter`             | Provides the date for the next third quarter moon phase.                                       |
| `Next First Quarter`             | Provides the date for the next first quarter moon phase.                                       |
| `Moon Altitude`                  | Provides the altitude of the moon in degrees.                                                  |
| `Moon Azimuth`                   | Provides the azimuth of the moon in degrees.                                                   |
| `Moon Parallactic Angle`         | Provides the parallactic angle of the moon in degrees.                                         |
| `Next Moon Phase`                | Provides the next moon phase and its date.                                                     |

## Contribution

Contributions are welcome! If you have any suggestions, issues, or feature requests, please open an issue or submit a pull request.

### Contributors

- [@ngocjohn](https://github.com/ngocjohn) — original author
- [@italo-lombardi](https://github.com/italo-lombardi) — v0.3.0 improvements

##

Enjoy tracking the lunar phases with the Lunar Phase integration for Home Assistant!

&copy; 2024–2026 Viet Ngoc

[https://github.com/ngocjohn/](https://github.com/ngocjohn/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
