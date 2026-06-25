def transform_match(match: dict) -> dict:
    """
    Transform one raw cricket match into a clean record.
    """

    transformed = {
        "match_id": match.get("id"),
        "match_name": match.get("name"),
        "match_type": match.get("matchType"),
        "status": match.get("status"),
        "venue": match.get("venue"),
        "match_date": match.get("date"),
        "match_datetime_gmt": match.get("dateTimeGMT"),
        "series_id": match.get("series_id"),
        "match_started": match.get("matchStarted"),
        "match_ended": match.get("matchEnded")
    }

    return transformed