""" Ru'yah AI """

from ruyah.categories.models import Category
from ruyah.tags.models import Tag
from ruyah.tasks import TASK_PRIORITIES


# LLM response format
RESPONSE_FORMAT = {
    "type": "json",
    "value": {
        "properties": {
            "task_list": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Task list name",
                        "maxLength": 32,
                    },
                    "description": {
                        "type": "string",
                        "description": "Task list description",
                        "maxLength": 256,
                    },
                    "tasks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "category": {
                                    "type": "string",
                                    "description": "Task category",
                                    "enum": [c.name for c in Category.objects.all()],
                                },
                                "title": {
                                    "type": "string",
                                    "description": "Task title",
                                    "maxLength": 32,
                                },
                                "description": {
                                    "type": "string",
                                    "description": "Task description",
                                    "maxLength": 256,
                                },
                                "deadline": {
                                    "type": "string",
                                    "description": "Task deadline in ISO 8601 format",
                                    "format": "date-time",
                                },
                                "priority": {
                                    "type": "string",
                                    "description": "Task priority",
                                    "enum": [p[1] for p in TASK_PRIORITIES],
                                },
                                "tags": {
                                    "type": "array",
                                    "description": "Task tags",
                                    "items": {
                                        "type": "string",
                                        "enum": [t.name for t in Tag.objects.all()],
                                    },
                                    "minItems": 1,
                                    "uniqueItems": True,
                                },
                            },
                            "required": [
                                "category",
                                "title",
                                "description",
                                "priority",
                            ],
                        },
                        "minItems": 3,
                        "uniqueItems": True,
                    },
                },
                "required": ["name", "description", "tasks"],
            },
        },
        "required": ["task_list"],
    },
}
