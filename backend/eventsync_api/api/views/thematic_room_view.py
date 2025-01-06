from core.models import ThematicRoom
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..serializers.thematic_room_serializers import ThematicRoomSerializer
from ..permissions import ReadOnly


@extend_schema_view(
    get=extend_schema(summary="List all thematic rooms", tags=["ThematicRoom"]),
    post=extend_schema(summary="Create a new thematic room", tags=["ThematicRoom"]),
)
class ThematicRoomListView(generics.ListCreateAPIView):
    """
    Visualização para listar e criar salas temáticas.
    """

    queryset = ThematicRoom.objects.all()
    serializer_class = ThematicRoomSerializer
    permission_classes = [IsAuthenticated | ReadOnly]


@extend_schema_view(
    get=extend_schema(summary="Retrieve a thematic room", tags=["ThematicRoom"]),
    put=extend_schema(summary="Update a thematic room", tags=["ThematicRoom"]),
    patch=extend_schema(
        summary="Partially update a thematic room", tags=["ThematicRoom"]
    ),
    delete=extend_schema(summary="Delete a thematic room", tags=["ThematicRoom"]),
)
class ThematicRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Visualização para detalhar, atualizar e deletar uma sala temática.
    """

    queryset = ThematicRoom.objects.all()
    serializer_class = ThematicRoomSerializer
    permission_classes = [IsAuthenticated | ReadOnly]
