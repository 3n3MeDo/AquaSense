from django.core.management.base import BaseCommand
from reservations.models import Course, Instructor

class Command(BaseCommand):
    help = 'Seeds the database with initial courses and instructors'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create Instructors
        jack, _ = Instructor.objects.get_or_create(
            name="Jack Marlin",
            defaults={
                "bio": "Expert in deep sea diving with 15 years of experience.",
                "specialization": "Wreck Diving",
                "photo": "https://randomuser.me/api/portraits/men/32.jpg"
            }
        )
        
        sarah, _ = Instructor.objects.get_or_create(
            name="Sarah Coral",
            defaults={
                "bio": "Marine biologist and photography expert.",
                "specialization": "Underwater Photography",
                "photo": "https://randomuser.me/api/portraits/women/44.jpg"
            }
        )

        # Create Courses
        courses = [
            {
                "title": "Open Water Diver Certification",
                "slug": "open-water-diver",
                "description": "Your first step into the underwater world. Get certified to dive anywhere! This course covers basic skills and safety procedures.",
                "price": 499.00,
                "duration": "3 Days",
                "difficulty": "Beginner",
                "image": "https://res.cloudinary.com/dp2ov37tr/image/upload/v1763854348/aquasense/aquasense/open_water.png",
                "instructor": jack,
                "is_popular": True
            },
            {
                "title": "Whale Shark Encounter",
                "slug": "whale-shark-encounter",
                "description": "A once-in-a-lifetime chance to swim alongside the gentle giants of the ocean. Snorkeling experience required.",
                "price": 250.00,
                "duration": "1 Day",
                "difficulty": "Beginner",
                "image": "https://res.cloudinary.com/dp2ov37tr/image/upload/v1763854352/aquasense/aquasense/whale_shark.png",
                "instructor": sarah,
                "is_popular": True
            },
            {
                "title": "Cenote Cavern Dive",
                "slug": "cenote-cavern-dive",
                "description": "Explore the breathtaking underwater cave systems of the Yucatan Peninsula. Requires Open Water certification.",
                "price": 180.00,
                "duration": "4 Hours",
                "difficulty": "Intermediate",
                "image": "https://res.cloudinary.com/dp2ov37tr/image/upload/v1763854354/aquasense/aquasense/cenote.png",
                "instructor": jack,
                "is_popular": False
            },
            {
                "title": "Reef Shark Exploration",
                "slug": "reef-shark-exploration",
                "description": "Observe magnificent reef sharks in their natural habitat. A thrilling adventure for certified divers.",
                "price": 220.00,
                "duration": "4 Hours",
                "difficulty": "Intermediate",
                "image": "https://res.cloudinary.com/dp2ov37tr/image/upload/v1763854350/aquasense/aquasense/coral_reef.png",
                "instructor": sarah,
                "is_popular": False
            },
             {
                "title": "Underwater Photography Course",
                "slug": "underwater-photography",
                "description": "Learn the art of capturing stunning images beneath the waves. Bring your own camera or rent one from us.",
                "price": 350.00,
                "duration": "2 Days",
                "difficulty": "Beginner",
                "image": "https://res.cloudinary.com/dp2ov37tr/image/upload/v1763854352/aquasense/aquasense/photography.png",
                "instructor": sarah,
                "is_popular": False
            },
            {
                "title": "Advanced Wreck Diving",
                "slug": "advanced-wreck-diving",
                "description": "Explore historic shipwrecks and learn advanced penetration techniques. Advanced Open Water required.",
                "price": 450.00,
                "duration": "3 Days",
                "difficulty": "Advanced",
                "image": "https://res.cloudinary.com/dp2ov37tr/image/upload/v1763854353/aquasense/aquasense/wreck_diving.png",
                "instructor": jack,
                "is_popular": False
            },
        ]

        for course_data in courses:
            Course.objects.get_or_create(
                slug=course_data['slug'],
                defaults=course_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
