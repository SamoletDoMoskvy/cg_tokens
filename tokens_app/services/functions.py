def _get_all_tokens(view):
    queryset = view.get_queryset().select_related()
    queryset = view.paginate_queryset(queryset)
    serializer = view.get_serializer(queryset, many=True)
    serializer = view.get_paginated_response(serializer.data)

    return serializer.data
