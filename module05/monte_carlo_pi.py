# monte_carlo_pi.py
import random
import math

def estimate_PI(num_points: int, seed: int | None = None) -> float:
    """
    Estimate the value of PI using a Monte Carlo method.

    Procedure:
      1) Sample points (x, y) uniformly in the unit square [0, 1] x [0, 1].
      2) Count how many fall inside the quarter unit circle: x^2 + y^2 <= 1.
      3) inside/total ≈ PI/4  ->  PI ≈ 4 * inside/total

    Parameters
    ----------
    num_points : int
        Number of random points to sample (>=1).
    seed : int | None, default None
        Seed for the random number generator. If None, no seeding is performed.

    Returns
    -------
    float
        Estimated value of PI.
    """
    if num_points <= 0:
        raise ValueError("num_points must be a positive integer")

    if seed is not None:
        random.seed(seed)

    inside = 0
    for _ in range(num_points):
        x = random.random()  # random x in [0,1)
        y = random.random()  # random y in [0,1)
        if (x * x + y * y) <= 1.0:
            inside += 1

    return 4.0 * inside / num_points


if __name__ == "__main__":
    # Demonstration of convergence with increasing number of points
    for n in [10**3, 10**4, 10**5, 10**6]:
        pi_hat = estimate_PI(n, seed=42)  # fixed seed for reproducibility
        err = abs(pi_hat - math.pi)
        print(f"N={n:>7,d}  ->  PI≈{pi_hat:.6f}  |  error={err:.6e}")

    # Show variability between different runs without setting the seed
    print("\nDifferent runs without seed (showing randomness):")
    n = 100_000
    for run in range(3):
        pi_hat = estimate_PI(n, seed=None)
        print(f"Run {run+1}: N={n:,} -> PI≈{pi_hat:.6f}")