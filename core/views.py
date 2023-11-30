from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Order
from core.serializers import EmployeeOrdersSerializer, ClientOrdersSerializer


@api_view(['GET'])
def get_orders_by_employee(request, pk):
    try:
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        query = f"""WITH employee_ranking AS (SELECT p.order_id as order_id, SUM(p.quantity) as total_amount, 
            SUM(p.price * p.quantity) as total_price FROM core_product as p GROUP BY p.order_id) 
            SELECT e.id, e.full_name, COUNT(o.client_id) as clients, SUM(total_amount) as total_amount, 
            SUM(total_price) as total_price FROM core_order as o 
            INNER JOIN core_employee as e ON o.employee_id = e.id 
            INNER JOIN employee_ranking as r ON o.id = r.order_id 
            WHERE e.id = {pk} """
        if month:
            query = query + f"AND date_part('month', o.date) = {month} "
        if year:
            query = query + f"AND date_part('year', o.date) = {year} "
        orders = Order.objects.raw(query + "GROUP BY e.id, e.full_name;")

        serializer = EmployeeOrdersSerializer(orders, many=True)

        return Response(serializer.data)
    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_employee_statistics(request):
    try:
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        query = f"""WITH employee_ranking AS (SELECT p.order_id as order_id, SUM(p.quantity) as total_amount, 
            SUM(p.price * p.quantity) as total_price FROM core_product as p GROUP BY p.order_id) 
            SELECT e.id, e.full_name, COUNT(o.client_id) as clients, SUM(total_amount) as total_amount, 
            SUM(total_price) as total_price FROM core_order as o 
            INNER JOIN core_employee as e ON o.employee_id = e.id 
            INNER JOIN employee_ranking as r ON o.id = r.order_id """
        if month:
            query = query + f"WHERE date_part('month', o.date) = {month} "
        if year:
            if month:
                query = query + f"AND date_part('year', o.date) = {year}"
            else:
                query = query + f"WHERE date_part('year', o.date) = {year} "
        orders = Order.objects.raw(query + "GROUP BY e.id, e.full_name;")

        serializer = EmployeeOrdersSerializer(orders, many=True)

        return Response(serializer.data)
    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_orders_by_clients(request, pk):
    try:
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        query = f"""WITH client_ranking AS (SELECT p.order_id as order_id, SUM(p.quantity) as total_amount, 
            SUM(p.price * p.quantity) as total_price FROM core_product as p GROUP BY p.order_id) 
            SELECT c.id, c.full_name, SUM(total_amount) as total_amount, 
            SUM(total_price) as total_price FROM core_order as o 
            INNER JOIN core_client as c ON o.client_id = c.id 
            INNER JOIN client_ranking as r ON o.id = r.order_id 
            WHERE c.id = {pk} """
        if month:
            query = query + f"AND date_part('month', o.date) = {month} "
        if year:
            query = query + f"AND date_part('year', o.date) = {year} "
        orders = Order.objects.raw(query + "GROUP BY c.id, c.full_name;")

        serializer = ClientOrdersSerializer(orders, many=True)

        return Response(serializer.data)
    except:
        return Response({'detail': 'Order does not exist'}, status=status.HTTP_400_BAD_REQUEST)
