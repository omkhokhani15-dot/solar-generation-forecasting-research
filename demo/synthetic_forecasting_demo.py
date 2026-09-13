"""Sanitized solar forecasting demonstration.

This example uses synthetic data only. It is intentionally independent of
the production forecasting implementation.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def make_synthetic_data(days=45, seed=42):
    rng = np.random.default_rng(seed)
    periods = days * 24
    time = pd.date_range("2025-01-01", periods=periods, freq="h")

    hour = time.hour.to_numpy()
    day_of_year = time.dayofyear.to_numpy()

    solar_shape = np.maximum(
        0.0,
        np.sin((hour - 6) / 12.0 * np.pi)
    )

    seasonal = 0.9 + 0.1 * np.sin(
        (day_of_year - 80) / 365.0 * 2 * np.pi
    )

    weather = np.clip(
        0.85 + 0.10 * rng.normal(size=periods),
        0.25,
        1.05,
    )

    generation_kw = 1000 * solar_shape * seasonal * weather
    generation_kw = np.clip(
        generation_kw + rng.normal(0, 18, periods),
        0,
        None,
    )

    df = pd.DataFrame(
        {
            "timestamp": time,
            "generation_kw": generation_kw,
            "hour": hour,
            "day_of_year": day_of_year,
            "solar_shape": solar_shape,
        }
    )

    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df["generation_lag_1"] = df["generation_kw"].shift(1)
    df["generation_lag_24"] = df["generation_kw"].shift(24)

    return df.dropna().reset_index(drop=True)


def main():
    df = make_synthetic_data()

    features = [
        "hour_sin",
        "hour_cos",
        "day_of_year",
        "solar_shape",
        "generation_lag_1",
        "generation_lag_24",
    ]

    split = int(len(df) * 0.8)
    train = df.iloc[:split]
    test = df.iloc[split:]

    model = RandomForestRegressor(
        n_estimators=150,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(train[features], train["generation_kw"])
    prediction = model.predict(test[features])

    mae = mean_absolute_error(test["generation_kw"], prediction)

    print(f"Synthetic demonstration MAE: {mae:.2f} kW")
    print("This result is synthetic and is not the private research result.")


if __name__ == "__main__":
    main()
