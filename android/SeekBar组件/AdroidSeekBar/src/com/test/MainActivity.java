package com.test;

import android.app.Activity;
import android.os.Bundle;
import android.widget.SeekBar;
import android.widget.SeekBar.OnSeekBarChangeListener;
import android.widget.TextView;

public class MainActivity extends Activity
{
	private TextView textView1;

	public void onCreate(Bundle savedInstanceState)
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.main);

		textView1 = (TextView) this.findViewById(R.id.textview1);
		SeekBar seekBar1 = (SeekBar) this.findViewById(R.id.seekbar1);
		seekBar1.setOnSeekBarChangeListener(new MyOnSeekBarChangeListener());

	}

	class MyOnSeekBarChangeListener implements OnSeekBarChangeListener
	{

		// ���������͵�ʱ��ᴥ�����¼�
		public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser)
		{
			textView1.setText("seekbar1�ĵ�ǰλ���ǣ�" + progress);
		}

		// ��ʾ�����￪ʼ�϶�
		public void onStartTrackingTouch(SeekBar seekBar)
		{
			textView1.setText("seekbar2��ʼ�϶�  " + seekBar.getProgress());
		}

		// ��ʾ����������϶�
		public void onStopTrackingTouch(SeekBar seekBar)
		{
			textView1.setText("seekbar1ֹͣ�϶�  " + seekBar.getProgress());

		}

	}
}