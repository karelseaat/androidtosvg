 # Binary Vector Graphics - Logo Design

This repository contains the source files for a vector graphics logo design created using Android's `<Vector>` library and Kotlin programming language. The logo is designed in two colors: dark red (#ea5555) and white (#ffffff).

## Features

- Designed for scalability to accommodate various screen sizes and resolutions.
- Optimized for efficient rendering to minimize resource consumption.
- Created using vector graphics, ensuring high-quality output regardless of the display density.

## Usage

To use this logo in your Android project, follow these steps:

1. Add the required dependencies to your `build.gradle` (Module) file:

```groovy
dependencies {
    implementation 'com.google.android:material:1.5.0'
}
```

2. Import the VectorDrawable into your XML layout file and assign it to an `ImageView`.

```xml
<ImageView
    android:id="@+id/logo"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:srcCompat="@drawable/logo" />
```

3. In your Kotlin or Java code, find the ImageView and set its size as needed:

```kotlin
val logo = findViewById<ImageView>(R.id.logo)
logo.layoutParams = ViewGroup.LayoutParams(size, size)
```

Replace `size` with the desired width or height of the logo in your specific context.

## Contributing

Pull requests are welcome! If you'd like to contribute, please open an issue describing your proposed changes before starting work.

## License

This project is licensed under [MIT License](LICENSE).

Enjoy using this vector graphics logo design in your projects!