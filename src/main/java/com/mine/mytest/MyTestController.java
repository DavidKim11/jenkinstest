package com.mine.mytest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyTestController {
	
	@GetMapping("/test")
	public String test() {
		return "This is a test.";
	}
}
