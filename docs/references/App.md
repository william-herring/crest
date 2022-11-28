# App

The ```App``` component specifies what is contained inside the app. This includes pages and configurations. For example, you may pass an ```entrypoint```
argument, which will redirect the '/' route to something else.
```python
MyApp = App([
    SamplePage()
], entrypoint='/sample')
```