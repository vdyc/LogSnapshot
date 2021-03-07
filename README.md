# LogSnapshot
Python project with UI to speed up log analysis

[![license][license]][license-url]

This tool was targeted to provide convenience for log analysis especially for well formatted large logs. 
For example [android logcat][logcat], a [pseudo log][logcat example] was used from project [fake-logcat][fake-logcat].
Log file are parsed when loading to this tool, user have full control to define condition matrix to combine the display 
condition such as Time / Tag Id / Debug Level / Filter / PID and etc.
User can also define your own file format for file parsing.

This tool borrowed the idea of filter from [TextAnalysisTool][TextAnalysisTool]. User can create and save filters in groups, 
so your efforts can be reused for future analysis

## Requirement

* Python 3.7+


## Getting Started

```sh
# Install dependencies
pip install -r requirements.txt

# Run LogSnapshot (with python 3)
python logSnapshot.py
```


## Usage

Support Win & Ubuntu



## Resources

* Android logcat format: [Android logcat format][logcat]
* Inspiration : [TextAnalysisTool][TextAnalysisTool]
* Log example : [Python Fake Logs][fake-logs]

## License
LogSnapshot is [MIT licensed](./LICENSE).


[//]: # (---------------------------------------------------------------------)

[//]: # (Resources)
[logcat]:     https://developer.android.com/studio/debug/am-logcat
[logcat example]: https://github.com/vdyc/fake-logcat/blob/master/examples/logcat_5000.log
[TextAnalysisTool]: https://textanalysistool.github.io/
[fake-logcat]: https://github.com/vdyc/fake-logcat

[//]: # (Badges)
[license]:     https://img.shields.io/badge/license-MIT-blue.svg
[license-url]: ./LICENSE
