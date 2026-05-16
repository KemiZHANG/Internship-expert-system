DEFAULT_VIEW = "assessment"
RESULTS_VIEW = "results"

VIEW_ORDER = (
    "assessment",
    "results",
    "explanation",
    "kb",
    "testing",
)


def normalize_view(view: str | None) -> str:
    if view in VIEW_ORDER:
        return view
    return DEFAULT_VIEW


def view_after_analysis(current_view: str | None) -> str:
    normalize_view(current_view)
    return RESULTS_VIEW
