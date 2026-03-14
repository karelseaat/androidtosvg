# Binary Vector Graphics – Logo Design

I built this logo because I needed a clean, scalable icon for an Android app—no SVG hacks, no PNGs in every density bucket. Just a single XML VectorDrawable, two colors (dark red `#ea5555` and white `#ffffff`), and zero dependencies beyond the Android framework.

## What’s in it

- **True vector** – scales to any size without blurring. Renders cleanly on 1x and 4x+ displays.
- **Lightweight** – ~2 KB XML, no bitmaps, no extra assets.
- **Ready to drop in** – works with `ImageView`, `Button`, `Toolbar`, anywhere you’d use a drawable.

## How to use it

1. Drop `logo.xml` into `res/drawable/`.
2. Reference it in your layout:

```xml
<ImageView
    android:id="@+id/logo"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:srcCompat="@drawable/logo" />
```

3. Adjust size at runtime (if needed):

```kotlin
val logo = findViewById<ImageView>(R.id.logo)
logo.layoutParams = ViewGroup.LayoutParams(size, size)
```

That’s it—no Material library required, though I left the dependency line in the original docs in case you’re using other Material components.

## Contributing

Found a bug or want to tweak the paths? Open an issue first with your idea—I’ll only merge pull requests that stay true to the vector-only constraint.

## License

[MIT License](LICENSE) — use it in personal or commercial projects. Just don’t claim you designed it.