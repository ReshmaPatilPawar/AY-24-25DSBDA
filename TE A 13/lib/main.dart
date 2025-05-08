import 'package:flutter/material.dart';

void main() {
  runApp(const HeartHealthApp());
}

class HeartHealthApp extends StatelessWidget {
  const HeartHealthApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.light(),
      darkTheme: ThemeData.dark(),
      themeMode: ThemeMode.system,
      debugShowCheckedModeBanner: false,
      home: const HeartFormPage(),
    );
  }
}

class HeartFormPage extends StatefulWidget {
  const HeartFormPage({Key? key}) : super(key: key);

  @override
  State<HeartFormPage> createState() => _HeartFormPageState();
}

class _HeartFormPageState extends State<HeartFormPage> with SingleTickerProviderStateMixin {
  final ageController = TextEditingController();
  final bpController = TextEditingController();
  final cholesterolController = TextEditingController();
  final heartRateController = TextEditingController();
  final stDepressionController = TextEditingController();

  final profileNameController = TextEditingController();
  final profileAgeController = TextEditingController();
  final profileEmailController = TextEditingController();
  final profilePhoneController = TextEditingController();
  final profileEmergencyController = TextEditingController();
  final profileAddressController = TextEditingController();

  String? selectedSex = "Male";
  String? selectedChestPain = "Typical Angina";
  String? selectedSugar = "No";
  String? selectedECG = "Normal";
  String? selectedExerciseAngina = "No";
  String? selectedSlope = "Flat";
  String? selectedVessels = "0";
  String? selectedThal = "Reversible Defect";

  late AnimationController _animationController;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _animationController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 500),
    );
    _scaleAnimation = CurvedAnimation(
      parent: _animationController,
      curve: Curves.easeInOutBack,
    );
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }

  void _submitForm() {
    final age = int.tryParse(ageController.text) ?? 0;
    final cholesterol = int.tryParse(cholesterolController.text) ?? 0;
    final stDepression = double.tryParse(stDepressionController.text) ?? 0.0;
    final heartRate = int.tryParse(heartRateController.text) ?? 0;

    String riskLevel;
    String advice;
    Color riskColor;

    if (age > 60 || cholesterol > 250 || stDepression > 2.0 || heartRate < 100) {
      riskLevel = "High";
      advice = "Please consult a cardiologist immediately. Maintain a heart-healthy diet and avoid stress.";
      riskColor = Colors.red;
    } else if (age > 45 || cholesterol > 200 || stDepression > 1.0) {
      riskLevel = "Moderate";
      advice = "Monitor your health regularly, exercise daily, and reduce salt and sugar intake.";
      riskColor = Colors.yellow[800]!;
    } else {
      riskLevel = "Low";
      advice = "Your heart health looks good. Maintain a healthy lifestyle and stay active.";
      riskColor = Colors.green;
    }

    _animationController.forward(from: 0.0);

    showDialog(
      context: context,
      builder: (_) => ScaleTransition(
        scale: _scaleAnimation,
        child: AlertDialog(
          title: const Text("Heart Health Report"),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                "Risk Level: $riskLevel",
                style: TextStyle(fontWeight: FontWeight.bold, color: riskColor, fontSize: 18),
              ),
              const SizedBox(height: 8),
              Text("Advice: $advice"),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text("OK"),
            ),
          ],
        ),
      ),
    );
  }

  void _openSettings() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Settings'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ListTile(
              leading: const Icon(Icons.edit),
              title: const Text('Edit Profile'),
              onTap: () {
                Navigator.of(context).pop();
                _editProfile();
              },
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text('Close'),
          )
        ],
      ),
    );
  }

  void _editProfile() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Edit Profile'),
        content: SingleChildScrollView(
          child: Column(
            children: [
              _buildTextField("Name", profileNameController),
              _buildTextField("Age", profileAgeController),
              _buildTextField("Email", profileEmailController),
              _buildTextField("Phone Number", profilePhoneController),
              _buildTextField("Emergency Contact Number", profileEmergencyController),
              _buildTextField("Address", profileAddressController),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: const Text('Save'),
          )
        ],
      ),
    );
  }

  Widget _buildTextField(String label, TextEditingController controller) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12.0),
      child: TextField(
        controller: controller,
        decoration: InputDecoration(
          labelText: label,
          border: const OutlineInputBorder(),
        ),
      ),
    );
  }

  Widget _buildDropdown(String label, List<String> items, ValueChanged<String?> onChanged, String? currentValue) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12.0),
      child: InputDecorator(
        decoration: InputDecoration(
          labelText: label,
          border: const OutlineInputBorder(),
        ),
        child: DropdownButtonHideUnderline(
          child: DropdownButton<String>(
            value: currentValue,
            isExpanded: true,
            onChanged: onChanged,
            items: items.map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
          ),
        ),
      ),
    );
  }

  void _callEmergencyContact() {
    final number = profileEmergencyController.text;
    if (number.isNotEmpty) {
      // You can integrate url_launcher here for actual phone call support.
      showDialog(
        context: context,
        builder: (_) => AlertDialog(
          title: const Text("Call Emergency Contact"),
          content: Text("Calling: $number"),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text("OK"),
            ),
          ],
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Heart Disease Prediction"),
        centerTitle: true,
        leading: IconButton(
          icon: const Icon(Icons.settings),
          onPressed: _openSettings,
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.call),
            onPressed: _callEmergencyContact,
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            _buildTextField("Age", ageController),
            _buildDropdown("Sex", ["Male", "Female"], (val) => setState(() => selectedSex = val), selectedSex),
            _buildDropdown("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"], (val) => setState(() => selectedChestPain = val), selectedChestPain),
            _buildTextField("Resting Blood Pressure (mm Hg)", bpController),
            _buildTextField("Cholesterol (mg/dl)", cholesterolController),
            _buildDropdown("Fasting Blood Sugar >120 mg/dl", ["Yes", "No"], (val) => setState(() => selectedSugar = val), selectedSugar),
            _buildDropdown("Resting ECG Results", ["Normal", "ST-T Abnormality", "Left Ventricular Hypertrophy"], (val) => setState(() => selectedECG = val), selectedECG),
            _buildTextField("Maximum Heart Rate", heartRateController),
            _buildDropdown("Exercise Induced Angina", ["Yes", "No"], (val) => setState(() => selectedExerciseAngina = val), selectedExerciseAngina),
            _buildTextField("ST Depression", stDepressionController),
            _buildDropdown("Slope of Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"], (val) => setState(() => selectedSlope = val), selectedSlope),
            _buildDropdown("Number of Major Vessels", ["0", "1", "2", "3"], (val) => setState(() => selectedVessels = val), selectedVessels),
            _buildDropdown("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"], (val) => setState(() => selectedThal = val), selectedThal),
            const SizedBox(height: 16),
            ElevatedButton(
              onPressed: _submitForm,
              child: const Text("Check Heart Health"),
            )
          ],
        ),
      ),
);
}
}