""" API views for ruyah.ai """

from huggingface_hub import InferenceClient
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from ruyah.ai import RESPONSE_FORMAT
from ruyah.ai.serializers import PromptSerializer


# Create your views here.
class AIViewSet(GenericViewSet):
    """AI API endpoints"""

    client = InferenceClient("mistralai/Mistral-Nemo-Instruct-2407")
    serializer_class = PromptSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def generate(self, request: Request) -> Response:
        """Generate task lists with tasks using AI"""

        # Data
        serializer = self.get_serializer(data=request.POST)

        # Data validation
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        messages = [
            {
                "role": "system",
                "content": "As a senior task manager, your role is to efficiently organize "
                "and manage comprehensive task lists. Focus on breaking down into manageable tasks, "
                "prioritizing them based on urgency and importance. Ensure to include deadlines, dependencies, "
                f"and any necessary resources required for each task. Format your response as following: {RESPONSE_FORMAT}",
            },
            {"role": "user", "content": serializer.validated_data["prompt"]},
        ]

        response = self.client.chat_completion(
            messages=messages,
            # response_format=RESPONSE_FORMAT,
            max_tokens=1024,
        )

        return Response(
            data={"response": response.choices[0].message.content},
            status=status.HTTP_200_OK,
        )
