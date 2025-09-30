import numpy as np

def power_output_vec(
    v: np.ndarray,
    prated: float = 15.0,
    v_in: float = 3.0,
    v_rated: float = 11.0,
    v_out: float = 25.0,
    interpolation: str = "linear",
) -> np.ndarray:
    """
    Vectorized version of the Project 1 power curve model.
    Works with NumPy arrays of any shape.

    Parameters
    ----------
    v : np.ndarray
        Wind speeds (any shape).
    prated : float, default 15.0
        Rated power (MW).
    v_in : float, default 3.0
        Cut-in wind speed (m/s).
    v_rated : float, default 11.0
        Rated wind speed (m/s).
    v_out : float, default 25.0
        Cut-out wind speed (m/s).
    interpolation : {"linear", "cubic"}, default "linear"
        Weighting function g(v) on [v_in, v_rated).

    Returns
    -------
    np.ndarray
        Power outputs with same shape as v.
    """
    v = np.asarray(v, dtype=float)

    if interpolation == "linear":
        g = (v - v_in) / (v_rated - v_in)
    elif interpolation == "cubic":
        g = (v ** 3) / (v_rated ** 3)
    else:
        raise ValueError('interpolation must be "linear" or "cubic"')

    # clamp g to [0, 1]
    g = np.clip(g, 0.0, 1.0)

    # piecewise definition using np.where
    p = np.where(
        (v < v_in) | (v >= v_out), 0.0,            # Region 1 & 4
        np.where(v >= v_rated, prated, g * prated) # Region 3 else Region 2
    )
    return p