print("hello world")

Duration calculateTimeDifference({
  required String startDate,
  required String endDate,
  required String startTime,
  required String endTime,
}) {
  // Parse the start and end dates
  DateTime startDateTime = DateTime.parse(startDate);
  DateTime endDateTime = DateTime.parse(endDate);

  // Combine the start date with the start time
  startDateTime = DateTime(
    startDateTime.year,
    startDateTime.month,
    startDateTime.day,
    int.parse(startTime.split(":")[0]),  // Hour
    int.parse(startTime.split(":")[1]),  // Minute
  );

  // Combine the end date with the end time
  endDateTime = DateTime(
    endDateTime.year,
    endDateTime.month,
    endDateTime.day,
    int.parse(endTime.split(":")[0]),  // Hour
    int.parse(endTime.split(":")[1]),  // Minute
  );

  DateTime currentDateTime = DateTime.now(); // Get the current date and time

  // If the current time is after the start time
  if (currentDateTime.isAfter(startDateTime)) {
    // Calculate the difference between current time and end time
    return endDateTime.difference(currentDateTime);
  } else {
    throw Exception("Current time is before the start date and time.");
  }
}



 Duration difference = calculateTimeDifference(
      startDate: startDate,
      endDate: endDate,
      startTime: startTime,
      endTime: endTime,
    );
