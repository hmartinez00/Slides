# RELATIONSHIPS

## ONE TO ONE
### Pasos preliminares
1. Nos apoyamos en el modelo user, y creamos otro modelo llamado phone.

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Phone.php"
protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_09_190213_create_phones_table.php"

> Nota: Este paso es crucial para garantizar las vinculaciones!

La clave foranea se establece asi: 
    $table->unsignedBigInteger('user_id');

"nombredelmodelo_id" (minusculas)

4. Migramos.

> Nota: El modelo que contiene a la clave foranea "pertenece a (BelongsTo)" el modelo que no la contiene.


### Vinculaciones
5. Vinculamos User con Phone

En "Slides\laravel\relationships\app\Models\User.php" creamos una funcion publica:

    public function phone(): HasOne
    {
        return $this->hasOne(Phone::class);
    }

Esto es para que cuando solicitemos $user->phone se nos devuelva todos los phone que tiene el usuario. Solo tiene uno, de manera que solo se devolvera uno (HasOne). Como usamos la convencion de nombres "user_id" en la clave foranea, ya laravel sabe que que debe acudir al campo "id" del modelo que estamos relacionando con "Phone".

Si la "foreing_key" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function phone(): HasOne
    {
        return $this->hasOne(Phone::class, "foreing_key", "field");
    }

6. Vinculamos Phone con User

En "Slides\laravel\relationships\app\Models\Phone.php" creamos una funcion publica:

    public function user():BelongsTo
    {
        return $this->belongsTo(User::class);
    }

Si la "foreing_key" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function user():BelongsTo
    {
        return $this->BelongsTo(User::class, "foreing_key", "field");
    }


> Hasta este punto culmina el proceso de vinculacion. El proximo paso es la creacion de la estructura de VIEWS o la APIS.


### Poblando la Base de datos
7. Creamos los Seeder para el User y el Phone.

8. En el "Slides\laravel\relationships\database\seeders\DatabaseSeeder.php" incorporamos el "call" a los seeder:

        $this->call([
            UserSeeder::class,
            PhoneSeeder::class,
        ]);

9. En el "Slides\laravel\relationships\database\seeders\UserSeeder.php" actualizamos:

        User::create([
            'id' => 1,
            'name' => 'example',
            'email' => 'example@example.com',
            'password' => Hash::make('12345678'),
        ]);

y en el "Slides\laravel\relationships\database\seeders\PhoneSeeder.php" actualizamos:

        Phone::create([
            'prefix' => +58,
            'phone_number' => 11111111,
            'user_id' => 1,
        ]);

10. Montamos la info con "php artisan bd:seed".

### Gestionando la VIEW

> Usaremos el modelo primario, el modelo donde NO esta la foreing_key.

11. Creamos el controlador de la vista "UserController".

12. En el "Slides\laravel\relationships\routes\web.php" creamos la ruta usando el controlador:

Route::get('/', [UserController::class, 'index'])->name('index');

13. En el "Slides\laravel\relationships\app\Http\Controllers\UserController.php" creamos la funcion:

    public function index()
    {
        $user = User::find(1);
        return view('index', compact('user'));
    }

14. Creamos finalmente la vista:

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>index</title>
    </head>
    <body>
        <h1>{{ $user->email }}</h1>
        <h1>{{ $user->phone->prefix }}</h1>
        <h1>{{ $user->phone->phone_number }}</h1>
    </body>
    </html>
```

### Gestionando la API
15. Creamos el Resource con:
    php artisan make:resource UserResource

16. En "Slides\laravel\relationships\app\Http\Resources\UserResource.php" modificamos el return:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phone' => '('.$this->phone->prefix.')'.$this->phone->phone_number,
        ];

17. En "Slides\laravel\relationships\routes\api.php" modificamos el Route:

Route::get('/user', function (Request $request) {
    $user = User::find(1);
    return new UserResource($user);
});

> Hasta este punto hemos gestionado la entrega de los datos en vista y en API (min 40:16).


## ONE TO MANY
> Para este tipo de relacion tendremos que modificar la relacion entre los modelos.

### Vinculaciones
1. En el modelo prioritario "Slides\laravel\relationships\app\Models\User.php" hacemos el cambio de "HasOne" a "HasMany".

    public function phones(): HasMany
    {
        return $this->hasMany(Phone::class);
    }

Con esto ya se ha construido la relacion ONE TO MANY.

### Repoblando la Base de datos
2. Añadimos otro dato con nuestros PhoneSeeder y comentamos el UserSeeder en el DatabaseSeeder para que no se ejecute y aplicamos "php artisan db:seed".

### Gestionando la VIEW
3. Actualizamos la vista:

```html
    <h1>{{ $user->name }} Phones:</h1>
    <ul>
    @foreach ($user->phones as $phone)
        <li>{{ $phone->prefix }} {{ $phone->phone_number }}</li>
    @endforeach
    </ul>  
```

### Gestionando la API
4. En el "Slides\laravel\relationships\app\Http\Resources\UserResource.php" Actualizamos el UserResource:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phones' => $this->phones,
        ];

> Aca hemos culminado el proceso para crear una relacion ONE TO MANY (min 47:21).

## MANYTOMANY
### Pasos preliminares
1. Creamos un nuevo modelo llamado "Role".

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Role.php"
protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_28_201223_create_roles_table.php"

4. Migramos.

### Creando tabla de Paso para vinculaciones
> Aca se emplea no una llave foranea sino una tabla de paso entro dos modelos para lograr las vinculaciones. La convencion de nomenclatura es la siguiente: modelo1_modelo2 (ordenados alfabeticamente).

5. Ceamos el archivo de migracion (No lleva modelo asociado!!) con php artisan make:migration create_role_user_table

6. (min 52:41) En "Slides\laravel\relationships\database\migrations\2023_08_28_203333_create_role_user_table.php" modificar el Schema para agregar las "foreing_key" como sigue:

        Schema::create('role_user', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('role_id');
            $table->unsignedBigInteger('user_id');
            $table->timestamps();
        });

Podriamos añadir algo de informacion extra.

        Schema::create('role_user', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('role_id');
            $table->unsignedBigInteger('user_id');
            $table->string('added_by')->nullable();
            $table->timestamps();
        });

7. Vovio a Migrar.

### Vinculaciones
8. Vinculamos User con Role

En "Slides\laravel\relationships\app\Models\User.php"

    public function roles():BelongsToMany
    {
        return $this->belongsToMany(Role::class);
    }
    public function roles():BelongsToMany
    {
        return $this->belongsToMany(Role::class)->withPivot('added_by');
    }

Si la "tabla_de paso" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function roles():BelongsToMany
    {
        return $this->belongsToMany(Role::class, 'role_user', 'user_id', 'role_id');
    }

9. vinculamos Role con User

En "Slides\laravel\relationships\app\Models\Role.php" creamos la funcion publica:

    public function users():BelongsToMany
    {
        return $this->belongsToMany(User::class);
    }
    public function users():BelongsToMany
    {
        return $this->belongsToMany(User::class)->withPivot('added_by');
    }

Si la "tabla_de paso" no respetara la convencion de laravel, habria que especificar dos parametros en la funcion:

    public function users():BelongsToMany
    {
        return $this->belongsToMany(User::class, 'role_user', 'user_id', 'role_id');
    }

### Repoblando la Base de datos
10. Creamos el Seeder pare el modelo Role.

11. En el "Slides\laravel\relationships\database\seeders\DatabaseSeeder.php" incorporamos el "call" a los seeder:

        $this->call([
            UserSeeder::class,
            PhoneSeeder::class,
            RoleSeeder::class,
        ]);

12. En el "Slides\laravel\relationships\database\seeders\UserSeeder.php"

        User::create([
            'id' => 1,
            'name' => 'example',
            'email' => 'example@example.com',
            'password' => Hash::make('12345678'),
        ]);
        User::create([
            'id' => 2,
            'name' => 'example2',
            'email' => 'example2@example2.com',
            'password' => Hash::make('12345678'),
        ]);
        User::create([
            'id' => 3,
            'name' => 'example3',
            'email' => 'example3@example3.com',
            'password' => Hash::make('12345678'),
        ]);

y en el "Slides\laravel\relationships\database\seeders\RoleSeeder.php" actualizamos:

        Role::create([
            'id' => 1,
            'name' => 'admin'
        ]);
        Role::create([
            'id' => 2,
            'name' => 'staff'
        ]);
        Role::create([
            'id' => 3,
            'name' => 'user'
        ]);
        Role::create([
            'id' => 4,
            'name' => 'guest'
        ]);

        // Aca vamos a hacer la asociacion!
        DB::table('role_user')->insert([
            'role_id' => 1,
            'user_id' => 1,
            'added_by' => 'hmartinez',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 2,
            'user_id' => 1,
            'added_by' => 'luis',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 1,
            'user_id' => 2,
            'added_by' => 'jose',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 3,
            'user_id' => 2,
            'added_by' => 'hmartinez',
        ]);
        DB::table('role_user')->insert([
            'role_id' => 4,
            'user_id' => 3,
            'added_by' => 'maria',
        ]);

13. Montamos la info con "php artisan bd:seed" (Aca hicimos un "refresh" previo para evitar montar info duplicada!).

### Gestionando la VIEW
14. Actualizamos la vista: 

```html
    <h1>{{ $user->name }} Roles:</h1>
    <ul>
    @foreach ($user->roles as $role)
        <li>{{ $role->name }} Added By: {{ $role->pivot->added_by}}</li>
    @endforeach
    </ul>  
```

### Gestionando la API
15. En el "Slides\laravel\relationships\app\Http\Resources\UserResource.php" Actualizamos el UserResource:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phones' => $this->phones,
            'roles' => $this->roles
        ];

> Aca culmina el proceso de MANY TO MANY (min 01:10:43)


## HAS ONE THROUGH
> Esta es el tipo de relacion que tiene un modelo con otro indirectamente, apoyandose en la relacion que tienen ambos, con un tercero.

### Pasos preliminares
1. Creamos otro modelo llamado phone.

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Sim.php"
protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_29_145616_create_sims_table.php"

> Nota: Este paso es crucial para garantizar las vinculaciones!

La clave foranea se establece asi: 
    $table->unsignedBigInteger('phone_id');

### Vinculaciones

4. Vinculamos Phone con Sim

En "Slides\laravel\relationships\app\Models\Phone.php" creamos una funcion publica:

    public function sim():HasOne
    {
        return $this->hasOne(Sim::class);
    }

5. Vinculamos Sim con Phone

En "Slides\laravel\relationships\app\Models\Sim.php" creamos una funcion publica:

    public function phone():BelongsTo
    {
        return $this->belongsTo(Phone::class);
    }

6. Vinculamos User con Sim "a traves" de Phone el cual ya esta relacionado con Sim.

En el "Slides\laravel\relationships\app\Models\User.php" creamos una funcion publica:

    public function phoneSim():HasOneThrough
    {
        return $this->hasOneThrough(Sim::class, Phone::class);
    }

Si no respetara la convencion de laravel, habria que especificar tres parametros en la funcion:

    public function phoneSim():HasOneThrough
    {
        return $this->hasOneThrough(Sim::class, Phone::class, [sim_param], [phone_param], [local_key]);
    }

### Repoblando la Base de datos
.

### Gestionando la VIEW
. Actualizamos la vista:

```html
    <h1>{{ $user->name }} Roles:</h1>
    <h3>{{ $user->phoneSim }}</h3>
    <ul>
    @foreach ($user->roles as $role)
        <li>{{ $role->name }} Added By: {{ $role->pivot->added_by}}</li>
    @endforeach
    </ul> 
```

### Gestionando la API
. 

> (min 01:19:17)


## HAS ONE THROUGH
> Para este tipo de relacion tendremos que modificar la relacion entre los modelos.

### Vinculaciones
1. En el "Slides\laravel\relationships\app\Models\Phone.php" hacemos el cambio de "HasOne" a "HasMany".

    public function sims():HasMany
    {
        return $this->hasMany(Sim::class);
    }

2. En el "Slides\laravel\relationships\app\Models\User.php" hacemos el cambio de "HasOneThrough" a "HasManyThrough".

    public function phoneSims():HasManyThrough
    {
        return $this->hasManyThrough(Sim::class, Phone::class);
    }

> (min 01:22:29)

## POLIMORFICAS
### Pasos preliminares
1. Creamos otro modelo llamado post e image.

2. Declaramos en:
"Slides\laravel\relationships\app\Models\Post.php" y en "Slides\laravel\relationships\app\Models\Image.php":
    protected $guarded = [];

3. Establecemos la estructura en el archivo de migracion:
"Slides\laravel\relationships\database\migrations\2023_08_30_165644_create_posts_table.php" y "Slides\laravel\relationships\database\migrations\2023_08_30_170049_create_images_table.php".

> Nota: Este paso es crucial para garantizar las vinculaciones!

La clave foranea se establece asi: 
            $table->unsignedBigInteger('imageable_id');
            $table->string('imageable_type');


"nombredelmodelo(able)_id" (minusculas)

### Vinculaciones
4. "Morfeamos" Image

En "Slides\laravel\relationships\app\Models\Image.php" creamos la funcion publica:

    public function imageable():MorphTo
    {
        return $this->morphTo();
    }

5. "Morfeamos" Post

En "Slides\laravel\relationships\app\Models\Post.php" creamos la funcion publica:

    public function image():MorphOne
    {
        return $this->morphOne(Image::class, 'imageable');
    }

6. "Morfeamos" User

En el "Slides\laravel\relationships\app\Models\User.php"

    public function image():MorphOne
    {
        return $this->morphOne(Image::class, 'imageable');
    }


### Repoblando la Base de datos
.

### Gestionando la VIEW
. Actualizamos la vista:

```html
    <h1>{{ $user->image->url }}</h1>
```

### Gestionando la API
. Actualizamos la API

En el "Slides\laravel\relationships\app\Http\Resources\UserResource.php" actualizamos el UserResource:

        return [
            'id' => $this->id,
            'name' => $this->name,
            'email' => $this->email,
            'phones' => $this->phones,
            'roles' => $this->roles,
            'image' => $this->image,
        ];

