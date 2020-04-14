import 'dart:convert';

import 'package:http/http.dart';
import 'package:flutter/material.dart';

void main() => runApp(MaterialApp(
  home: MyApp(),
));
class MyApp extends StatefulWidget {
 
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final _formKey = GlobalKey<FormState>();  

  final myController = TextEditingController();

  var result = '';
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
        appBar: AppBar(
          title: Text('Salary Prediction App'),
        ),
        body: Container(
         child: Form(
           key:_formKey,
           child: Column(
             crossAxisAlignment: CrossAxisAlignment.start,
             children:<Widget>[
               Image.network(
  'https://149402609.v2.pressablecdn.com/wp-content/uploads/2016/06/clinical-psych_salary.gif',
),
               TextFormField(
                    controller: myController,
                    decoration: const InputDecoration(  
                    icon: const Icon(Icons.scatter_plot),  
                    hintText: 'Years of experience',  
                    labelText: 'Enter years of experience',  
            ),  
               ),
               Container(  
              padding: const EdgeInsets.only(left: 150.0, top: 20.0),  
             
              child: new RaisedButton(  
                  
                 child: const Text('Predict',style: TextStyle(fontSize: 20,color: Colors.white)),  
                  
                  onPressed: predict, 
              )),  
               Padding(
                 padding: const EdgeInsets.all(15.0),
                 child: Center(
                   
                   child: Text(result)
                 ),
               )
             ]
           ),
          
         ), 
        )
      );
  }
  predict() async{
    setState(() {
      this.result='Predicting...Please wait for the result';
    });
    String url = 'https://predict-salary-flask.herokuapp.com/predict?experience='+myController.text;
  Response response = await get(url);
  // sample info available in response
 
  String json = response.body;
  var data =jsonDecode(json);
  var result = data['result'];
  var salary=double.parse((double.parse(result)).toStringAsFixed(2));
  print(json);
  
    setState(() { this.result= 'Estimate Salary should be around - Rs.'+salary.toString(); });
      }
}