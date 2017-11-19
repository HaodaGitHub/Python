package com.test.service;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.test.service.domain.LoginResult;
import com.test.tools.HttpUtils;

import android.util.Log;

public class LoginService
{

	public LoginResult login2Server(String name, String pwd){
		//ģ�M��ꑣ���ꑳɹ���ַ
		String path = "http://42.185.61.153:8020/web1/ok.json";
		
		//ģ�M��ꑣ����ʧ����ַ
		//String path = "http://42.185.61.153:8020/web1/error.json";
		
		String jsonStr = HttpUtils.getJsonContent(path);
		
		Log.i("main", jsonStr);
		JSONObject jsonObj = JSON.parseObject(jsonStr);
		boolean flag = (Boolean) jsonObj.get("flag");
		String desc = (String) jsonObj.get("desc");
		Log.i("main", "flag=" + flag);
		
		LoginResult result = new LoginResult();
		result.setFlag(flag);
		result.setDesc(desc);
		return result;
	}
	
}
