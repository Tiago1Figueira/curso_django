from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 682327604},
        'instalacao_windows': {'titulo': '', 'vimeo_id': 690291392},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
