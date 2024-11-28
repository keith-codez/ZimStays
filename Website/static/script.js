document.addEventListener('DOMContentLoaded', function () {
  // Part 1: Date Validation Logic
  const startDateInput = document.getElementById('start-date');
  const endDateInput = document.getElementById('end-date');

  startDateInput.addEventListener('change', function () {
    const startDate = new Date(startDateInput.value);
    
    if (startDate) {
      // Add one day to the selected start date
      const minEndDate = new Date(startDate);
      minEndDate.setDate(minEndDate.getDate() + 1);

      // Format the minEndDate to 'YYYY-MM-DD'
      const formattedMinEndDate = minEndDate.toISOString().split('T')[0];

      // Set the minimum value for end date to be the day after the start date
      endDateInput.min = formattedMinEndDate;
    }
  });

  // Part 2: Guest Details Toggle Logic
  const toggleGuestDetailsButton = document.getElementById('toggle-guest-details');
  const guestDetails = document.getElementById('guest-details');

  // Toggle guest details section visibility
  toggleGuestDetailsButton.addEventListener('click', function () {
    guestDetails.classList.toggle('d-none'); // Show or hide guest details
  });

  // Function for Increment and Decrement
  function setupIncrementDecrement(buttonId, inputId, increment) {
    const button = document.getElementById(buttonId);
    const input = document.getElementById(inputId);

    button.addEventListener('click', function () {
      const currentValue = parseInt(input.value);
      const newValue = increment ? currentValue + 1 : Math.max(currentValue - 1, input.min);
      input.value = newValue;
    });
  }

  // Setup for Adults
  setupIncrementDecrement('adult-increment', 'adults', true);
  setupIncrementDecrement('adult-decrement', 'adults', false);

  // Setup for Children
  setupIncrementDecrement('children-increment', 'children', true);
  setupIncrementDecrement('children-decrement', 'children', false);

  // Setup for Rooms
  setupIncrementDecrement('rooms-increment', 'rooms', true);
  setupIncrementDecrement('rooms-decrement', 'rooms', false);
});



 