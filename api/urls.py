from rest_framework import routers
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from marketcap.views import CoinGechkoCoinList,MarketCapList,SearchCoin
from coindetail.views import CryptoNews,CoinDetail,CoinDetailAllMarket,CoinDetailInfo,CoinMiniChart
from exchange.views import ExchangeDetail,ExchangeValume
from staking.views import StakingCoinViewSet
router = routers.DefaultRouter()

# router.register(r'MarketCap', MarketCapViewSet)
router.register(r'stakingList',StakingCoinViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # path('search/', SearchAPIView.as_view()),
    path('marketcap/', MarketCapList.as_view()),
    path('marketcapGechko/', CoinGechkoCoinList.as_view()),
    path('coindetail/' , CoinDetail.as_view()),
    path('coindetailinfo/' , CoinDetailInfo.as_view()),
    path('coindetailallmarket/' , CoinDetailAllMarket.as_view()),
    path('minichart/' ,CoinMiniChart.as_view()),
    path('exchange/', ExchangeDetail.as_view()),
    path('exchangeValume/', ExchangeValume.as_view()),
    path('search/', SearchCoin.as_view()),
    path('cryptonews/',CryptoNews.as_view()),
    
    # path('wishlispost/',WishlistPost.as_view()),
    # path('deletewishlist/',DeleteWishlist.as_view()),
    # path('changepassword/',SendMailForNewEmail.as_view()),
    # path('password/reset/confirm/', PasswordResetView.as_view(),),

]\
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
               + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)