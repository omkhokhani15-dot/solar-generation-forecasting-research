# Research Methodology

## 1. Problem definition

The research addresses short-horizon solar generation forecasting. The objective is to estimate future photovoltaic generation while accounting for solar position, weather variability and operational effects.

The public repository documents the methodology at a high level rather than exposing the production implementation.

## 2. Site and physical feature layer

The research workflow uses solar-geometry concepts including:

- solar declination
- hour angle
- solar-window masking
- clear-sky irradiance
- extraterrestrial radiation
- incidence-related geometry

These features provide a physical reference against which observed irradiance and generation can be evaluated.

## 3. Environmental and operational signals

Relevant signals include:

- global horizontal irradiance
- clear-sky index
- air temperature
- wind speed
- relative humidity
- rainfall
- aerosol/cloud proxies
- thermal effects
- soiling
- degradation

The purpose is to separate changes in generation caused by solar availability from changes associated with environmental or operational conditions.

## 4. Weather-regime analysis

The research uses regime-oriented features to distinguish conditions such as:

- clear
- cloudy
- volatile

Signals can include clear-sky divergence, cloud ramps, rainfall, humidity and irradiance variability.

Regime information is useful because forecast error characteristics are not uniform across weather conditions.

## 5. Forecasting architecture

The underlying research architecture combines temporal feature extraction with regime-aware probabilistic modelling. The research workflow includes temporal convolution, bidirectional sequence encoders, attention-based pooling and mixture-of-experts / Gaussian-mixture output concepts.

The production implementation is deliberately not reproduced here.

## 6. Calibration

Forecast outputs are statistically calibrated at the site level. Calibration is intended to improve the reliability of predicted generation and uncertainty estimates.

The associated implementation uses isotonic calibration.

## 7. Backtesting

Historical observations are compared against forecast outputs using error metrics including MAE. Backtesting is used to evaluate whether model refinements improve forecast accuracy rather than relying only on training performance.

## 8. Public demonstration boundary

This repository contains only a sanitized methodology and synthetic demonstration.

Excluded from the public repository:

- production source code
- private operational datasets
- client/site identifiers
- trained model weights
- credentials and API keys
- private cloud/Colab links
- production configuration
- proprietary operational logic
