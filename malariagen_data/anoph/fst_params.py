"""Parameter definitions for Fst functions."""

from typing import Optional, Literal

import pandas as pd
from typing_extensions import Annotated, TypeAlias

from . import base_params

# N.B., window size can mean different things for different functions
window_size: TypeAlias = Annotated[
    int,
    "The size of windows (number of sites) used to calculate statistics within.",
]
cohort_size_default: Optional[base_params.cohort_size] = None
min_cohort_size_default: base_params.min_cohort_size = 15
max_cohort_size_default: base_params.max_cohort_size = 50

clip_min: TypeAlias = Annotated[
    Optional[float],
    """
    Minimum value for Fst. Values below this are clipped to this value.
    """,
]

df_pairwise_fst: TypeAlias = Annotated[
    pd.DataFrame,
    """
    A dataframe of pairwise Fst and standard error values. It has
    4 columns:
    `cohort1` and `cohort2` are the two cohorts,
    `fst` is the value of the Fst between the two cohorts,
    `se` is the standard error.
    """,
]

annotation: TypeAlias = Annotated[
    Optional[Literal["standard error", "Z score"]],
    """
    How to annotate the upper-right corner of the plot. Default behaviour (None) is using Fst, other options
    are using the standard error (if annotation is 'standard error') or the Z score of the two
    cohorts being the same (if annotation is 'Z score').
    """,
]
