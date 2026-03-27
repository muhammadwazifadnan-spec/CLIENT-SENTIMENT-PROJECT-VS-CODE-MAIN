# dashboard_service.py

def build_dashboard_data(user_id, period=None, source_type=None):
    """
    Returns the same dict structure your user dashboard expects:
    {
      period, source_type,
      month_labels, line_complaint, line_non,
      scenario_labels, scenario_complaint, scenario_non,
      pct_complaint, pct_non
    }
    """
    # TODO: move your existing dashboard calculations here.
    # Use user_id to filter records for that user.
    # Use period + source_type as optional filters.

    dashboard_data = {
        "period": period or "",
        "source_type": source_type or "",
        "month_labels": [],
        "line_complaint": [],
        "line_non": [],
        "scenario_labels": [],
        "scenario_complaint": [],
        "scenario_non": [],
        "pct_complaint": 0,
        "pct_non": 0
    }

    return dashboard_data
