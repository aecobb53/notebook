# Angular

## Resources

CLI - https://angular.io/cli



## installing

#### Angular

```
npm install -g @angular/cli

cd <parent directory>

ng new <new application name (will create directory and associated files)>
```

#### Packages

```
npm install --save-dev <name>

# or

npm install --save <name>
```
Then add it to the `angular.json` file but it has to be an activation path. this is annoying!
They are either added to the styles or scripts under build in the angular.json file

List
```
npm install --save-dev bootstrap
npm install --save-dev jquery
npm install --save-dev popper.js

npm install --save lodash
```

If you recently cloned a repo, run `npm install` to install everything its missing

## Startign the service

```
ng serve
```


## Styling component
 
You can either add htm/css directly using `styles` or a path in `stylesUrl`


## IF
You can set an element to only show up if its value exists with `*`'s:
```html
<div *ngIf="mediaItem.watchedOn">Watched on {{ mediaItem.watchedOn }}</div>
```
If the if statement `*ngIf="mediaItem.watchedOn"` returns false, the element will not show up on the DOM. If you want to have multiple elements associated with the same if, you can wrap them
```html
<ng-template [ngIf]="mediaItem.watchedOn">
    <div>Watched on {{ mediaItem.watchedOn }}</div>
</ng-template>
```

## For loop

The syntax `let <item> of <array>` is important for the `for` loop

The ngClass looks for the css stuff to assign if its applies and doesnt if it doesnt. 

```html
<selection>
    <mw-media-item *nmFor="let mediaItem of mediaItems"
    [mediaItem]="mediaItem"
    (delete)="onMediaItemDelete($event)"
    [ngClass]="{ 'medium-movies': mediaItem.medium === 'Movies', 'medium-series': mediaItem.medium === 'Series'}"></mw-media-item>
</selection>
```


