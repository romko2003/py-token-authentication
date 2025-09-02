from rest_framework.routers import DefaultRouter
from .views import (
    GenreViewSet, CinemaHallViewSet, ActorViewSet,
    MovieViewSet, MovieSessionViewSet, OrderViewSet
)

app_name = "cinema"

router = DefaultRouter()
router.register("genres", GenreViewSet, basename="genre")
router.register("cinema_halls", CinemaHallViewSet, basename="hall")
router.register("actors", ActorViewSet, basename="actor")
router.register("movies", MovieViewSet, basename="movie")
router.register("movie_sessions", MovieSessionViewSet, basename="session")
router.register("orders", OrderViewSet, basename="order")

urlpatterns = router.urls
