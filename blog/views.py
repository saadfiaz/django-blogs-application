from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post 


def get_date(post):
    return datetime.strptime(post["date"], "%Y-%m-%d")
# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request,'blog/index.html', {"posts": latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by('date')
    return render(request, 'blog/all-posts.html', {"posts":all_posts})

def post_details(request,slug):
    result = Post.objects.get(slug=slug)
    return render(request, 'blog/post-detail.html', {"post":result, "tags": result.tags.all()})


all_p = [
    {
    
        "slug": "mountain-hiking",
        "image": "mountains.jpg",
        "author": "Alice Explorer",
        "date": "2024-11-01",
        "title": "Mountain Hiking",
        "excerpt": "There’s nothing like reflecting on life while standing atop a mountain...",
        "content": "Mountain hiking is an exhilarating experience, perfect for both the adventurous and the introspective. Imagine trudging up rugged trails, every step bringing you closer to a view that feels like a reward from the universe itself. The fresh air, the smell of pine, and the quiet only nature can offer—it’s like a natural meditation. And sure, your legs might feel like jelly by the time you reach the peak, but the sense of accomplishment makes every sore muscle worth it. Plus, there's always the descent to look forward to—a mix of thrill and careful footing!"
    },
    {
        "slug": "sunset-beach-walk",
        "image": "beach.jpg",
        "author": "Ben Shoreline",
        "date": "2024-10-25",
        "title": "Sunset Beach Walk",
        "excerpt": "A walk on the beach at sunset is nature’s therapy session.",
        "content": "Walking along the beach at sunset isn’t just beautiful; it’s therapeutic. There’s something about the waves gently kissing the shore and the sky turning shades of orange and pink that makes everything feel right in the world. Each step in the sand feels like a slow, calming release of tension as the ocean breeze plays with your hair. And if you’re lucky, maybe you'll spot some playful dolphins or friendly seagulls. The worries of the day seem to vanish with the setting sun, leaving you with a calm that only the ocean can offer. Perfect for soul searching—or just a good Instagram photo!"
    },
    {
        "slug": "camping-tips",
        "image": "camping.jpg",
        "author": "Carter Woods",
        "date": "2024-09-20",
        "title": "Top Camping Tips",
        "excerpt": "Here’s what they don’t tell you about camping: it’s 50% planning, 50% forgetting stuff.",
        "content": "Camping sounds like a simple outdoor escape, but the reality can be an adventure all its own! You might think you’ve packed everything, only to discover you forgot the one thing you really needed—like bug spray or a flashlight. Nature has a funny way of reminding us we’re not quite as prepared as we think! But it’s all part of the fun. From cozying up in a sleeping bag under the stars to cooking over an open fire (and trying not to burn dinner), camping is all about embracing the unexpected. Just don’t forget the marshmallows, because every camping trip deserves a good s’more!"
    },
    {
        "slug": "city-nightlife-guide",
        "image": "city.jpg",
        "author": "Dana Vibe",
        "date": "2024-09-10",
        "title": "Exploring City Nightlife",
        "excerpt": "Discover the charm and buzz of city nightlife in this guide.",
        "content": "City nightlife is a world of its own, filled with lights, sounds, and endless energy. From rooftop bars with breathtaking views to hidden speakeasies where you feel like you’ve traveled back in time, there’s something for everyone. You can dance till dawn or just enjoy people-watching in a busy plaza—either way, the city never sleeps, and neither will you! Street food stalls with late-night snacks are lifesavers when you need a quick bite after hours of exploring. The best part? The cityscape under the night sky has a charm you can’t find anywhere else, and every corner holds a new discovery."
    },
    {
        "slug": "desert-adventures",
        "image": "desert.jpg",
        "author": "Ella Sands",
        "date": "2024-08-15",
        "title": "Desert Adventures",
        "excerpt": "When it’s just you, the sand, and a sky full of stars.",
        "content": "Desert adventures are like no other. The open, seemingly endless landscape makes you feel both tiny and completely free. As you traverse the dunes, the sun may be hot, but there’s a certain peace in the solitude of the desert. And when night falls, the stars come out in full force, lighting up the sky in a way you rarely see elsewhere. Desert nights are chilly, and sitting around a campfire with friends, sharing stories, is the perfect way to end the day. Plus, sandboarding down a massive dune is an adrenaline rush you won’t forget anytime soon!"
    },
    {
        "slug": "river-rafting",
        "image": "river.jpg",
        "author": "Frank Rapids",
        "date": "2024-07-05",
        "title": "The Thrill of River Rafting",
        "excerpt": "Buckle up! River rafting is a wild, water-fueled ride.",
        "content": "River rafting is the ultimate thrill for water lovers and adventure seekers alike. The fast-flowing rapids keep you on the edge, with each turn offering a fresh rush of excitement. It’s just you, the raft, and the river, moving in sync with every twist and drop. As the water splashes and rocks the boat, there’s no time for second thoughts—it’s a live-in-the-moment experience! Once you reach calmer waters, the sense of accomplishment is immense. And yes, you’ll probably end up drenched, but every drop is a badge of honor in this heart-pounding journey."
    },
    {
        "slug": "forest-camping",
        "image": "woods.jpg",
        "author": "Grace Woodsy",
        "date": "2024-06-28",
        "title": "Forest Camping Adventures",
        "excerpt": "Getting lost in the woods can be therapeutic—until it’s not.",
        "content": "Forest camping is an adventure filled with the sounds of nature and a sense of peace. It’s just you, the trees, and maybe a squirrel or two stealing food. As you set up camp and settle in, you realize how serene the woods can be—until it gets a little too quiet. Sleeping under towering trees with a canopy of stars above is an experience like no other. And when morning comes, the forest comes alive with chirping birds and beams of sunlight filtering through the leaves. Forest camping is a reminder of the simple joys that come with disconnecting from the world and reconnecting with nature."
    }
]