package com.mine.mytest;

import java.util.Properties;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyTestController {
	
	@GetMapping("/test")
	public String test() {
		Properties properties = System.getProperties();
        
        // 전체 리스트 key=value 형태로 출력
        properties.forEach((key, value) -> {
            System.out.println(key + " = " + value);
        });
		return "This is a test.";
	}
}
