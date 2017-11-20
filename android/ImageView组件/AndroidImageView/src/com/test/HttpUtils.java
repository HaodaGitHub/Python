package com.test;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpUtils
{
	private final static String URL_PATH = "http://42.185.61.153:8020/web1/deskclock.png";// ������·ͼƬ��·��

	public HttpUtils() {
	}

	/**
	 * �������л�ȡͼƬ��Ϣ����������ʽ����
	 * 
	 * @return
	 */
	public static InputStream getImageViewInputStream() throws IOException {
		InputStream inputStream = null;

		URL url = new URL(URL_PATH);
		if (url != null) {
			HttpURLConnection httpURLConnection = (HttpURLConnection) url
					.openConnection();
			httpURLConnection.setConnectTimeout(3000);// �������ӳ�ʱ��ʱ��
			httpURLConnection.setRequestMethod("GET");
			httpURLConnection.setDoInput(true);
			
			int response_code = httpURLConnection.getResponseCode();
			if (response_code == 200) {
				inputStream = httpURLConnection.getInputStream();
			}
		}
		return inputStream;
	}

}
