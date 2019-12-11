from rest_framework import serializers

class NewsSerializer(serializers.Serializer):
    keywords = serializers.ListField()

    def to_representation(self, data):

        return {
            "news": [{
                "ranking": 0.89,
                "content": "First news...",
                "reference": "https://wwww.eluniversal.com.mx/notica.html"
            }, {
                "ranking": 0.75,
                "content": "Second news...",
                "reference": "https://wwww.excelsior.com.mx/notica.html"
            }, {
                "ranking": 0.56,
                "content": "Third news...",
                "reference": "https://media.jornada.com.mx/ultimas/notica.html"
            }]
        }
