package com.mine.mytest;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MytestApplication {

	public static void main(String[] args) {
		String commandPath = System.getProperty("sun.java.command");
		System.out.print(commandPath);
		SpringApplication.run(MytestApplication.class, args);
	}

}
