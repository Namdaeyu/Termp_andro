package kr.ac.pusan.cs.android.app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends AppCompatActivity {

    private WebView mWebView;
    private WebSettings mWebSettings;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mWebView = (WebView) findViewById(R.id.webView);
        mWebView.setWebChromeClient(new WebChromeClient()); //ChromeView
        mWebSettings = mWebView.getSettings(); //세팅 등록
        mWebSettings.setJavaScriptEnabled(true); //자바스크립트 허용

        try {
            mWebView.loadUrl("http://10.0.2.2:8080");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
