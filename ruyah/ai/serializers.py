""" Serializers for ruyah.ai """

from rest_framework import serializers


# Create your serializers here.
class PromptSerializer(serializers.Serializer):
    """Serialize prompts"""

    prompt = serializers.CharField(
        max_length=256,
        required=True,
        allow_blank=False,
        allow_null=False,
        help_text="Prompt",
    )
