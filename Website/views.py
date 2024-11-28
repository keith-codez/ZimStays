from django.shortcuts import render, get_object_or_404, redirect
from.models import Home, Reservation, City, Contact
from django.http import HttpResponse
from django.template import loader
from .forms import ReservationForm, ContactForm
from datetime import date 
from django.db.models import Q




def search_homes(request):
    cities = City.objects.all()  # Fetch all cities from the database
    return render(request, 'index.html', {'cities': cities})

# Create your views here.
def index (request):
    cities = City.objects.all()
    return render(request, 'index.html', {'cities': cities})

def location(request):
    # Get the city filter from the GET request
    city_filter = request.GET.get('city', None)

    # If a city filter is provided, filter homes by that city
    if city_filter:
        # Filter homes where the city matches the city selected by the user
        homes = Home.objects.filter(city__name=city_filter)
    else:
        # If no city filter is applied, show all homes
        homes = Home.objects.all()

    # Get the list of available cities for the location dropdown
    cities = City.objects.all()

    context = {
        "homes": homes,
        "cities": cities,  # Pass cities to the template for the location dropdown
        "city_filter": city_filter,  # Optionally pass the selected city filter
    }
    return render(request, "location.html", context)

def home_detail(request, home_id):
    home = Home.objects.get(id=home_id)
    context = {"home": home}
    return render(request, "home_detail.html", context)


  

def reservations(request, home_id):
    home = Home.objects.get(id=home_id)
    context = {"home": home}
    return render(request, "reservations.html", context)


def make_reservation(request, home_id):
    home = get_object_or_404(Home, id=home_id)
    
    # Capture the dates from the query parameters
    check_in_date = request.GET.get('check_in_date')
    check_out_date = request.GET.get('check_out_date')

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.home = home
            reservation.save()
            return redirect('reservation_success')
    else:
        # Pre-fill the form with the dates if they exist in the URL
        initial_data = {}
        if check_in_date:
            initial_data['check_in_date'] = check_in_date
        if check_out_date:
            initial_data['check_out_date'] = check_out_date
        
        form = ReservationForm(initial=initial_data)

    # Render the reservation page and pass the dates along with the form
    return render(request, 'reservations.html', {
        'form': form,
        'home': home,
        'check_in_date': check_in_date,
        'check_out_date': check_out_date
    })

def reservation_success(request):
    return render(request, 'reservation_success.html')


def filter_homes(request):
    if request.method == "GET":
        # Fetch query parameters with default values if empty
        destination = request.GET.get('destination', '').strip()
        arrival_date = request.GET.get('arrival_date', '').strip()
        departure_date = request.GET.get('departure_date', '').strip()
        guests = request.GET.get('guests', '').strip()

        # Validate required fields
        if not destination or not arrival_date:
            return render(request, 'filtered_homes.html', {
                'homes': [],
                'error': 'Please provide both a destination and an arrival date.'
            })

        # Attempt to parse arrival and departure dates
        try:
            arrival_date = date.fromisoformat(arrival_date)
        except ValueError:
            return render(request, 'filtered_homes.html', {
                'homes': [],
                'error': 'Invalid arrival date format.'
            })

        if departure_date:
            try:
                departure_date = date.fromisoformat(departure_date)
            except ValueError:
                return render(request, 'filtered_homes.html', {
                    'homes': [],
                    'error': 'Invalid departure date format.'
                })
        else:
            departure_date = None

        # Convert guests to an integer with a default value of 1
        try:
            guests = int(guests) if guests else 1
        except ValueError:
            return render(request, 'filtered_homes.html', {
                'homes': [],
                'error': 'Guests must be a valid number.'
            })

        # Filter homes based on the criteria
        homes = Home.objects.filter(
            city_id=destination,
            available_from__lte=(departure_date if departure_date else arrival_date),
        ).filter(
            Q(available_to__gte=arrival_date) | Q(available_to__isnull=True)
        ).filter(
            guests__gte=guests
        )

        # Exclude homes with conflicting reservations
        if departure_date:
            homes = homes.exclude(
                reservation__check_in_date__lt=departure_date,
                reservation__check_out_date__gt=arrival_date
            )
        else:
            homes = homes.exclude(
                reservation__check_out_date__gt=arrival_date
            )

        return render(request, 'filtered_homes.html', {'homes': homes})

    # Handle cases where the request method is not GET
    return render(request, 'filtered_homes.html', {'homes': []})

def about_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('contact_us_success')
    else:
        form = ContactForm()

    return render(request, 'about_us.html', {'form': form})

def contact_us_success(request):
    return render(request, 'contact_success.html')


def coming_soon(request):
    return render(request, 'coming_soon.html')
