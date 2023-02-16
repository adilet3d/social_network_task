# from django_filters import rest_framework as filters
# from mainapp.models import Like, DisLikes


# class DateLikesFilter(filters.FilterSet):
#     start_date = filters.DateFilter(field_name="created_at__date", lookup_expr="gte")
#     end_date = filters.DateFilter(field_name="created_at__date", lookup_expr="lte")

#     class Meta:
#         model = Like
#         fields = ['start_date', 'end_date']


# class DateDisLikesFilter(filters.FilterSet):
#     start_date = filters.DateFilter(field_name="created_at__date", lookup_expr="gte")
#     end_date = filters.DateFilter(field_name="created_at__date", lookup_expr="lte")

#     class Meta:
#         model = DisLikes
#         fields = ['start_date', 'end_date']