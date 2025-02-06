print("hello world")

//timer coundown start





late Timer _timer;
  int? _start; // OTP expiry time in seconds
  bool _isExpired = false;

//important for this part
  @override
  void dispose() {
    _timer.cancel(); // Ensure the timer is cancelled when widget is disposed
    super.dispose();
  }

  void _startTimer() {
    _timer = Timer.periodic(Duration(seconds: 1), (timer) {
      if (_start > 0) {
        setState(() {
          _start--;
        });
      } else {
        setState(() {
          _isExpired = true;
        });
        _timer.cancel(); // Stop the timer when expired
      }
    });
  }


//ui part
Center(
        child: _isExpired
            ? Text("OTP Expired", style: TextStyle(fontSize: 24, color: Colors.red))
            : Text("Time remaining: $_start seconds", style: TextStyle(fontSize: 24)),
      ),


//ticket table reservation api call area  status true


  if(value.status==true){
    //intha mari condition irukum athula intha line add panniko
intha api cal la vara  colsebooking time kuda 60
var secount=colsebookingtime*60;
setstate((){
  _start=secount;
})
 _startTimer();
  }







// bloc line
  baseResponse?.data = baseResponse.data != null
          ? List<AddAttendees>.from(
              baseResponse.data.map((data) => AddAttendees.fromJson(data)))
          : null;

// ui screen
//init function top add the variable ,i this allready declear the variable
 List<AddAttendees> addAttendees=[]
 bool addAttendees_status=false;


if(value.status!=false && value.data.length!=0){
  setStates((){
    addAttendees=value.data;
    addAttendees_status=true;
  });
}

//contineu button

if(addAttendees_status){
  setStetes((){
    activeStep=activeStep+1
  });
}





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




///latest update code


Duration calculateTimeDifference({
  required String startDate,
  required String endDate,
  required String startTime,
  required String endTime,
}) {
// Parse the starting date and time
  DateTime startDateTime = parseDateTime(startingDate, startingTime);

  // Parse the ending date and time
  DateTime endDateTime = parseDateTime(endingDate, endingTime);

  DateTime currentDateTime = DateTime.now(); // Get the current date and time

  // If the current time is after the start time
  if (currentDateTime.isAfter(startDateTime)) {
    // Calculate the difference between current time and end time
    return endDateTime.difference(currentDateTime);
  } else {
    return  Duration();
  }
}


DateTime parseDateTime(String date, String time) {
  // Parse the date (we will ignore time portion from the date string)
  DateTime datePart = DateTime.parse(date);

  // Split the time into hours and minutes
  List<String> timeParts = time.split(":");
  int hour = int.parse(timeParts[0]);
  int minute = int.parse(timeParts[1]);

  // Combine the date and time
  return DateTime(datePart.year, datePart.month, datePart.day, hour, minute);
}



 Duration difference = calculateTimeDifference(
      startDate: startDate,
      endDate: endDate,
      startTime: startTime,
      endTime: endTime,
    );


///time to add 5.30 minues
String addTime(String timeStr) {
  final DateFormat format = DateFormat("hh:mm");
  DateTime time = format.parse(timeStr);
  
  // Add 5 hours and 30 minutes
  time = time.add(Duration(hours: 5, minutes: 30));
  
  // Return the updated time in 12-hour AM/PM format
  return DateFormat("hh:mm a").format(time);
}

//dynamic data create model
class DynamicData {
  final dynamic data; // Can be any type of data

  DynamicData({
  
    this.data,
  });

  // Manually create the fromJson method
  DynamicData fromJson(Map<String, dynamic> json) {
    return DynamicData(
      data: json['data'],  // This can be dynamic
    );
  }

  // Manually create the toJson method
  Map<String, dynamic> toJson() {
    return {
      'data': data,
    };
  }
}



