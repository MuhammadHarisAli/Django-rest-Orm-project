from django.db.models import Q, Sum, F

from rest_framework import status, generics
from rest_framework.response import Response

from .models import DataSetModel
from .serializers import DataSetSerializer


class DataSet(generics.ListAPIView):
    serializer_class = DataSetSerializer
    queryset = DataSetModel.objects.all()

    def list(self, request, *args, **kwargs):
        group_by_fields = request.query_params.getlist('group_by_fields')

        filter_end_date = request.query_params.get('filter_end_date_field')
        filter_start_date = request.query_params.get('filter_start_date')
        filter_exact_date = request.query_params.get('filter_exact_date')
        filter_channel = request.query_params.get('filter_channel')
        filter_country = request.query_params.get('filter_country')
        filter_os = request.query_params.get('filter_os')
        filter_impressions = request.query_params.get('filter_impressions')
        filter_clicks = request.query_params.get('filter_clicks')
        filter_installs = request.query_params.get('filter_installs')
        filter_spend = request.query_params.get('filter_spend')
        filter_revenue = request.query_params.get('filter_revenue')

        order_by = request.query_params.get('order_by')
        select_fields = request.query_params.getlist('select_fields')
        query = self.queryset
        q_list = []
        if filter_channel:
            q_list.append(Q(channel=filter_channel))
        if filter_country:
            q_list.append(Q(country=filter_country))
        if filter_os:
            q_list.append(Q(os=filter_os))
        if filter_impressions:
            q_list.append(Q(impressions=filter_impressions))
        if filter_clicks:
            q_list.append(Q(clicks=filter_clicks))
        if filter_installs:
            q_list.append(Q(installs=filter_installs))
        if filter_spend:
            q_list.append(Q(spend=filter_spend))
        if filter_revenue:
            q_list.append(Q(filter_revenue=filter_revenue))
        if filter_end_date:
            q_list.append(Q(date__lte=filter_end_date))
        if filter_start_date:
            q_list.append(Q(date__gte=filter_start_date))
        if filter_exact_date:
            q_list.append(Q(date=filter_exact_date))

        annotate = {}

        if 'CPI' in group_by_fields:
            annotate['CPI'] = ( Sum(F('spend')) / Sum(F('installs')))
            group_by_fields.remove('CPI')

        for group_by in group_by_fields:
            annotate[group_by] = Sum(group_by)

        try:
            result = query.filter(*q_list).values(*select_fields ).annotate(**annotate).order_by(order_by)
        except exception as ProgrammingError:
            # log.error(filter_list_variables, select_fields_variables, group_by_data, order_by_data)
            return Response(
                {
                    'success': False,
                    'detail': 'error in query params',
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {
                'success': True,
                'data': list(result),
            },
            status=status.HTTP_200_OK
        )
