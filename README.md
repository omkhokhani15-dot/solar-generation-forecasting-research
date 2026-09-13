# solar-generation-forecasting-research

> Public research portfolio demonstrating an applied approach to short-horizon solar generation forecasting.

## Research focus

This project studies solar generation forecasting with emphasis on:

- solar geometry and clear-sky reference features
- weather and irradiance-derived signals
- thermal and soiling/degradation effects
- weather-regime classification
- time-series feature extraction
- probabilistic forecasting
- statistical calibration
- backtesting and forecast-error evaluation

**Important:** This repository is a sanitized research demonstration. Production implementation, private datasets, site identifiers, model artifacts, credentials, operational configuration, and proprietary feature-engineering details are intentionally excluded.

## Research workflow

The underlying research workflow is organised into three stages:

1. **Site Development Lab** — site-level preprocessing, solar geometry, thermal modelling, weather-regime features and baseline modelling.
2. **Universal Brain Trainer** — a hybrid deep-learning forecasting architecture using temporal convolution, bidirectional LSTM encoders, attention pooling and a mixture-of-experts / Gaussian-mixture output.
3. **Pilot / Backtest Engine** — model inference, calibration, 24-hour forecasting and historical backtesting.

## Selected technical components

### Solar geometry

The workflow derives features such as solar declination, hour angle, solar-window masking, incidence geometry and extraterrestrial-radiation normalization.

### Physical and environmental effects

The research pipeline considers clear-sky irradiance, air temperature, wind speed, relative humidity, rainfall, aerosol/cloud proxies, soiling, degradation and thermal lag.

### Weather regimes

Operating conditions are classified using signals such as clear-sky index, cloud-ramp behaviour, humidity, rainfall and irradiance variability.

### Probabilistic forecasting

The research architecture uses specialised regime-aware experts and probabilistic outputs to represent forecast uncertainty.

### Calibration and validation

The workflow includes site-level statistical calibration and historical backtesting using forecast-error metrics such as MAE.

## Selected research result

The associated research work reported a reduction in MAE from **101 kW to 87 kW**, corresponding to a **14% improvement** after model refinement and calibration.

This figure describes the associated research work; the underlying production dataset is not published in this repository.

## Public demonstration

`demo/synthetic_forecasting_demo.py` contains a small, reproducible demonstration using synthetic solar-generation data. It is intentionally independent of the production implementation.

## Repository structure
Author
```text
solar-generation-forecasting-research/
├── README.md
├── methodology/
│   └── research-methodology.md
├── demo/
│   └── synthetic_forecasting_demo.py
├── results/
│   └── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```
Author

Om Khokhani
Research Analyst | Renewable Energy & Power Markets | Quantitative Research



